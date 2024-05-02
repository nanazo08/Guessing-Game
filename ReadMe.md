# Guessing Game Server

This a simple guessing game server thats been enhanced by adding features that make it more fun to use. this code is implemented in Python using sockets. The Players connect to the server and guess a randomly generated number based on their chosen difficulty level and receive feedback until they guess correctly. There will be a leaderboard that shows the ranking of players based on their scores.



1. cd desktop
- i changed the directory to desktop folder

2. cd Enhanced-Guessing-Game/
- I navigated the folder i named 'Enhanced-Guessing-Game'

3. git clone https://github.com/nanazo08/Guessing-Game
- I cloned the github repository with the url in my current directory

4. cd Guessing-Game
- I moved into the newly clooned repository i just created.

5. git add Gserver.py(the name of the file of my code)
- I Prepare the changes made to the file named "Gserver.py" to be saved for later.

6. git commit -m "Added new functions to enhanced the code.
- I commit the changes i made using a descriptive message

7. git add Gclient.py
- Prepare the changes made to the file named "Gclient.py" to be saved for later.

8. git commit -m "Added extra Features to client"
- I commit the changes i made using a descriptive message

9. git push origin main
- I pushed the commited changes i just made to the main branch of the repository on Github.

The implementation on how my Guessing game Server Program works. this shows the interaction of the server and the client.

1. Imports
    - I used modules like `socket`, `threading`, `random`, `json`, and `time`.

2. **Setup**: I initializes variables like `host`, `port`, and `banner`.

3. **Data Handling**: I initializes empty dictionaries `user_data` and `leaderboard` to store player data and leaderboard information respectively. It defines functions `load_user_data()` and `save_user_data()` to load and save player data to a JSON file.

4. **Game Logic**: 
    - `generate_random_int(difficulty)`: Generates a random number based on the chosen difficulty level.
    - `handle_client(conn, addr)`: This function handles the interaction with each client:
        - Sends a banner message to the client.
        - Receives the player's name and chosen difficulty level.
        - Validates the difficulty level.
        - Generates a random number based on the chosen difficulty level and prompts the client for guesses.
        - Provides feedback on guesses (higher/lower).
        - Calculates the score based on the number of tries and time taken.
        - Updates user data, leaderboard, and sends necessary information back to the client.
        - Handles exceptions and closes the connection.

5. **Leaderboard Display**: 
    - `display_leaderboard()`: Sorts the leaderboard in descending order of scores and displays it.

6. **Server Setup**: 
    - Creates a socket, binds it to the specified host and port, and listens for incoming connections.

7. **Main Loop**: 
    - Accepts incoming connections and creates a new thread to handle each client's interaction.

The server continuously listens for new client connections, and each client interaction is handled independently, allowing multiple clients to play the guessing game concurrently.

***Connecting to the Server:***

1. On another device or terminal, run a client script or use Telnet to connect to the server's IP address and port (7777).
2. Follow the instructions provided by the client script to enter your name and choose a difficulty level (easy, medium, or hard).

***Playing the Game:***

1. Upon connection, the server will ask you to guess a randomly generated number.
2. Input your guess and press Enter.
3. The server will give feedback on your guess, indicating if you should guess higher or lower.
4. Continue guessing until you correctly identify the number.

***Scoring:***

1. Your score is calculated based on the number of attempts and time taken to guess the number.
2. Rapid guesses within a time limit may earn you a bonus.

***Viewing the Leaderboard:***

1. Once the game is finished, the server will present a leaderboard showing top scores.
2. Compare your score with others to see your ranking.

***Replaying or Exiting:***

1. You can play multiple times by reconnecting to the server and following the prompts.
2. To end the game, close the client connection or stop the server script.