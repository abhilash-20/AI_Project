# AI Tic-Tac-Toe using Minimax Algorithm

An intelligent Tic-Tac-Toe game where the player competes against an AI agent powered by the Minimax Algorithm.

## Project Overview

This project demonstrates the implementation of Artificial Intelligence in game development using the Minimax Algorithm. The AI agent evaluates all possible future game states and always chooses the optimal move, making it impossible to defeat.

The project is developed using Python and Tkinter for the graphical user interface.

---

## Features

* Human vs AI gameplay
* AI opponent using Minimax Algorithm
* Interactive GUI using Tkinter
* Restart game functionality
* Win, Lose, and Draw detection
* Intelligent move prediction

---

## Technologies Used

* Python
* Tkinter
* Minimax Algorithm
* Recursive Search

---

## How the AI Works

The AI uses the Minimax Algorithm, a decision-making algorithm commonly used in game theory and artificial intelligence.

The algorithm:

1. Simulates all possible future moves
2. Evaluates board states
3. Maximizes the AI’s chances of winning
4. Minimizes the opponent’s chances

### Minimax Formula

```text
Minimax(node) =
    max(children)   → AI Turn
    min(children)   → Player Turn
```

---

## Project Structure

```text
AI_Project/
│
├── tic_tac_toe.py
├── README.md
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/abhilash-20/AI_Project.git
```

### 2. Open Project Folder

```bash
cd AI_Project
```

### 3. Run the Program

```bash
python tic_tac_toe.py
```

---

## Game Rules

* Player uses **X**
* AI uses **O**
* The first to align 3 symbols horizontally, vertically, or diagonally wins
* If all cells are filled without a winner, the match is a draw

---

## Screenshots

Add screenshots of:

* Main game interface
* AI winning
* Draw condition
* Gameplay example

---

## Learning Outcomes

This project helped in understanding:

* Artificial Intelligence basics
* Adversarial Search
* Recursive Algorithms
* Game Tree Evaluation
* GUI Programming with Tkinter

---

## Future Improvements

Possible enhancements:

* Difficulty levels
* Alpha-Beta Pruning
* Score tracking
* Sound effects
* Dark mode UI
* Web-based multiplayer version

---

## Author

Abhilash Kashyap

---

## License

This project is created for educational and learning purposes.
