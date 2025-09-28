# snake-game
🐍 Enhanced Python Snake Game
This is a classic Snake game built using the Pygame library, featuring persistent high score tracking, a clean user interface, and optional sound integration.

✨ Features
Persistent High Score: Tracks and saves the highest score achieved in a local file (highscore.txt).

Start Menu: A clear introductory screen with game instructions.

Pause Functionality: Press P during gameplay to pause and resume.

Dynamic Speed: The snake's speed increases slightly every time it eats food, increasing the challenge.

Clear Score Display: Shows the current score and the high score during the game.

Sound Integration: Includes placeholders for background music, food consumption, and game over sounds (optional).

🛠️ Requirements
You need Python 3 and the Pygame library installed to run this game.

pip install pygame

🚀 How to Run
Save the provided code as a Python file (e.g., snake_game.py).

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the game using:

python snake_game.py

🕹️ Controls
Key

Action

Up Arrow

Move Up

Down Arrow

Move Down

Left Arrow

Move Left

Right Arrow

Move Right

SPACE

Start Game (from menu)

P

Pause / Resume Game

Q

Quit Game (from menu)

🎧 Sound Note (Optional)
The code attempts to load sound files (background.mp3, eat.wav, and gameover.wav).

If these files are not present in the same directory as the script, the game will print a message to the console and will run perfectly fine without sound. To enable sounds, simply place your own .mp3 and .wav files with those names into the game directory.

💾 High Score Management
The game automatically saves the high score to a file named highscore.txt in the same directory. If you want to reset the high score, simply delete this file.
