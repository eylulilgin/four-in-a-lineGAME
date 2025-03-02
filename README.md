# Four in a Line Game

## Overview
The **Four in a Line Game** is a Python-based program that determines the winner in a grid-based game similar to "Connect Four." The program checks for four consecutive pieces of the same type (either 'r' for red or 'y' for yellow) in rows, columns, or diagonals.

## Features
- Accepts a 2D list representing the game board.
- Checks for four consecutive identical symbols ('r' or 'y').
- Supports checking in horizontal, vertical, and diagonal directions.
- Returns the winner ('r' or 'y') if four in a row is found, otherwise returns `None`.

## Installation
To run this project, ensure you have **Python 3.x** installed on your system.

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/four-in-line.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd four-in-line
   ```
3. **Run the script:**
   ```bash
   python FourInLine.py
   ```

## Usage
1. The program contains one primary function:
   - `four_in_line(board)`: Checks a 2D list (game board) for a winner.
2. The board should be a list of lists containing '.', 'r', or 'y'.
3. Running the script prints the winner ('r' or 'y') or `None` if no winner is found.

## Example Output
```
Board:
[['.', '.', '.', '.', '.'],
 ['.', 'r', '.', 'y', '.'],
 ['.', 'r', '.', 'r', '.'],
 ['.', 'r', 'y', 'y', '.'],
 ['y', 'r', 'r', 'y', 'y']]

Output: r
```

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.
