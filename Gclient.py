import socket
import json

host = input("Enter the server host IP address: ")
port = 7777

def play_game():
    s = socket.socket()
    s.connect((host, port))

    data = s.recv(1024)
    print("\n== Guessing Game (Enhanced) ==\n")
    print(data.decode().strip())

    while True:
        user_input = input("Input: ").strip()
        if not user_input:
            print("Please enter a valid input.")
            continue
        s.sendall(user_input.encode())
        print()
        reply = s.recv(1024).decode().strip()

        if "Correct" in reply:
            print(reply)
            user_history = s.recv(1024).decode().strip()
            #print("User History:", user_history)  # Print user history for debugging
            user_data = json.loads(user_history)
            print("\n== Your History ==\n")
            print(f"Name: {user_data['name']}")
            print(f"Score: {user_data['score']}")
            print(f"Difficulty: {user_data['difficulty']}\n")
            break
        print(reply)
        continue

    s.close()

while True:
    play_game()
    repeat = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if repeat != "yes":
        break
