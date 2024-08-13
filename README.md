# Dice Game

## Overview

This Python-based Dice Game offers a fun and interactive way to roll dice with different options. The game features ASCII art representations of dice faces and allows the user to choose between paying different amounts to roll specific dice or rolling a standard die without payment.

## Features

- **ASCII Art Dice Faces:** The game displays visually appealing dice faces using ASCII art.
- **Multiple Dice Options:** Users can choose between:
  - A 6-sided die for 10 Rs.
  - A 5-sided die for 5 Rs.
  - A standard 6-sided die without payment.
- **Interactive Gameplay:** Players can choose to roll the dice as many times as they like or exit the game at any time.

## How to Play

### Choose Your Dice:

- The game will prompt you to select one of three dice options.
  - Enter `1` for a 6-sided die (10 Rs).
  - Enter `2` for a 5-sided die (5 Rs).
  - Enter `3` for a standard 6-sided die (free of charge).

### Process Payment:

- If you choose options `1` or `2`, you will need to enter your payment.
- If you pay more than required, the game will give you change.

### Roll the Dice:

- After choosing your dice, you can roll it by typing `yes`.
- The game will display the corresponding dice face based on the roll result.
- Type `no` to exit the game.

### Exit:

- You can exit the game anytime by entering `no` when prompted.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the `dice.py` file.
2. Ensure Python is installed on your system.
3. Run the game by executing the following command in your terminal:

   ```bash
   python dice.py
4.Follow the on-screen instructions to play the game.

## Example Output
Choose your dice option:
1. For a 6-sided die, you must pay 10 Rs
2. For a 5-sided die, you must pay 5 Rs
3. For not paying money
Enter your choice (1, 2, or 3): 1
Enter your payment (minimum 10 Rs): 10
Roll the dice? (yes/no): yes
<br>
┌─────────┐<br>
│ ● ● │<br>
│ ● │<br>
│ ● ● │<br>
└─────────┘<br>
4.Roll the dice? (yes/no): no
Exiting the game.

### Contributing
Feel free to fork this repository and submit pull requests for any improvements or additional feature

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.