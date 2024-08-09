# GTAV_-steering_wheel
## Project: Steering Wheel Emulator for Games like GTA, Mafia, Cyberpunk, Far Cry, and Others

# *How to Use?*
## The program has 4 files:
## - [main.py](https://github.com/Sergeiprogrammer/GTAV_-steering_wheel?tab=readme-ov-file#other-file-criticall-need-and-he-in-all-situation-must-be-installed)
## - [main_no_gamepad.py](https://github.com/Sergeiprogrammer/GTAV_-steering_wheel?tab=readme-ov-file#main_no_gamepadpy-1)  
## **!! DO NOT UNINSTALL ANY FILES, ALL FILES ARE CRITICALLY NEEDED !!**

# Selecting Files
## Check if your game supports a gamepad or not.
### There are 3 ways to check:
### 1. Start the program with `main.py`, go to the Steam library of your game, and Steam will automatically tell you if the game supports a gamepad.
### 2. Check in the game settings.
### 3. If it's difficult for you, just search on Google :)

# main.py
## Who should select this file?
### Select this file if your game supports a gamepad.

# main_no_gamepad.py
## Who should select this file?
### Select this file if your game *does not* support a gamepad.

# Setup Program
## 1. First, [install Python](https://youtu.be/nU2Egc3Zx3Q?si=UKn9doIC49yTroGD).
## 2. Second, install the necessary libraries by running the "install_all" script (if you have any problems, check the "Bugs" section below).
## 3. Thirdly, select your language and after that enter “1” (for constant steering) first set the steering wheel and then the dead zone.
## 4. Fourth, after completing the previous steps, start either `main.py` or `main_no_gamepad.py`, input "2" to start the game (my program works with both legal and illegal copies on Steam, Epic Games, and more), and enjoy :)

# For Those Interested in How It Works
## My program gets information about the wheel using Pygame. When you select the calibration mode and turn your wheel left or right, the program understands that left is one coordinate and right is another coordinate. Based on these coordinates, it determines the amount of input needed for the virtual gamepad stick or keyboard button.

# BUGS

## If the program says that something is not found, try searching the internet for how to manually install the necessary libraries.
### Example:
- pygame: `pip install pygame`
- keyboard: `pip install keyboard`
- vgamepad: `pip install vgamepad`

## If the program says "wheel not found," your wheel might not be supported by Pygame or is not connected. If it's not connected, check the documentation for your wheel, install any required plugins, or look for help on YouTube.

## If the program has other errors that are not solved in my documentation, please report them in the Issues section of my GitHub repository
