import socket
import threading
import random
import json
import time

host = input("Enter the server host IP address: ") 
port = 7777
banner = "Enter your name: "

#store data
user_data = {}
leaderboard = []

#history
def load_user_data():
    global user_data
    try:
        with open("Players_History.json", "r") as file:
            data = file.read()
            if data:
                user_data = json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
 #save data to json
def save_user_data():
    with open("Players_History.json", "w") as file:
        json.dump(user_data, file)

#generate random int
def generate_random_int(difficulty):
    if difficulty == 'easy':
        return random.randint(1, 50)
    elif difficulty == 'medium':
        return random.randint(1, 100)
    elif difficulty == 'hard':
        return random.randint(1, 500)
    
#client connection to server
def handle_client(conn, addr):
    try: #banner mssg to client
        conn.sendall(banner.encode())
        player_name = conn.recv(1024).decode().strip()
        #Prompts level of difficulty
        conn.sendall(b"Choose difficulty level (easy, medium, hard):\n")
        difficulty = conn.recv(1024).decode().strip().lower()

        # ensure the Validity
        while difficulty not in ['easy', 'medium', 'hard']:
            conn.sendall(b"Invalid difficulty level. Please choose again (easy, medium, hard):\n")
            difficulty = conn.recv(1024).decode().strip().lower()
        #generate random int based on the choice of difficulty
        while True:
            guessme = generate_random_int(difficulty)
            conn.sendall(b"Enter your guess:\n")
            start_time = time.time() # start timing
            tries = 0
            #continuesly receives the client guess
            while True:
                try:
                    client_input = conn.recv(1024)
                    if not client_input:
                        save_user_data()
                        return
                    #the server will decode the guess
                    guess = int(client_input.decode().strip())
                    tries += 1
                    # Calculate score using the number of tries and time
                    if guess == guessme:
                        score = 1000 // tries
                        elapsed_time = time.time() - start_time
                        if elapsed_time < 5:  # If the user guesses rapidly
                            conn.sendall(b"You guessed rapidly!\n")
                        conn.sendall(f"Correct Answer! You won!\nYour score: {score}\n".encode())

                        # Check if user exists with the same name and difficulty
                        if player_name in user_data and user_data[player_name]['difficulty'] == difficulty:
                            # Update score if the new score is higher
                            if score > user_data[player_name]['score']:
                                user_data[player_name]['score'] = score
                        else:
                            user_data[player_name] = {'score': score, 'difficulty': difficulty}


                        # Update leaderboard
                        leaderboard.append({'name': player_name, 'score': score, 'difficulty': difficulty})
                        save_user_data()
                        display_leaderboard()
                        #sends the user dat
                        conn.sendall(json.dumps({'name': player_name, 'score': score, 'difficulty': difficulty}).encode())
                        break
                    #feedback
                    elif guess > guessme:
                        conn.sendall(b"Guess Lower!\n")
                    elif guess < guessme:
                        conn.sendall(b"Guess Higher!\n")
                #auto save
                except ConnectionResetError:
                    save_user_data()
                    return
    #connection close
    except ConnectionAbortedError:
        pass
    finally:
        conn.close()


#leaderboard list in descending order
def display_leaderboard():
    global leaderboard
    print("\n== Leaderboard ==\n")
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    for i, player in enumerate(sorted_leaderboard):
        print(f"Rank {i+1}:")
        print(f"Name: {player['name']}")
        print(f"Score: {player['score']}")
        print(f"Difficulty: {player['difficulty']}\n")

#connection of the serveer and client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

load_user_data()
print(f"Server is listening on {host}:{port}")

while True:
    conn, addr = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
