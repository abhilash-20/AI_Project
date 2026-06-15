# Classical Artificial Intelligence Algorithms in Python

This repository contains implementations of multiple classical Artificial Intelligence algorithms developed using Python. The project demonstrates important AI concepts such as adversarial search, optimization, probabilistic reasoning, and game-playing intelligence.

The repository currently includes:

1. AI Tic-Tac-Toe using Minimax Algorithm
2. Alpha-Beta Pruning Tree Visualization
3. Hidden Markov Model using Viterbi Algorithm

---

# Project Overview

This project showcases practical implementations of fundamental AI algorithms commonly studied in Artificial Intelligence and Machine Learning courses.

Each implementation focuses on a different area of AI:

| Project            | AI Concept                             |
| ------------------ | -------------------------------------- |
| Tic-Tac-Toe AI     | Adversarial Search / Game AI           |
| Alpha-Beta Pruning | Search Optimization                    |
| HMM + Viterbi      | Probabilistic AI / Sequence Prediction |

The implementations include graphical visualizations, recursive algorithms, probability modeling, and intelligent decision-making.

---

# Included Projects

## 1. AI Tic-Tac-Toe using Minimax Algorithm

An intelligent Tic-Tac-Toe game where the player competes against an unbeatable AI agent.

### Features

* Human vs AI gameplay
* AI decision making using Minimax
* GUI using Tkinter
* Restart functionality
* Win/Loss/Draw detection

### AI Concept

```text id="5dy6qq"
Minimax(node) =
    max(children)   → AI Turn
    min(children)   → Player Turn
```

---

## 2. Alpha-Beta Pruning Tree Visualization

A visualization-based implementation of the Alpha-Beta Pruning algorithm used to optimize Minimax search trees.

### Features

* MAX/MIN tree visualization
* Alpha and Beta tracking
* Pruned branch identification
* Graph generation using Graphviz

### Pruning Condition

```text id="9kmxal"
β ≤ α
```

When this condition becomes true, unnecessary branches are pruned to improve efficiency.

---

## 3. Hidden Markov Model using Viterbi Algorithm

Implementation of a Hidden Markov Model (HMM) using the Viterbi Algorithm to predict the most likely hidden state sequence.

### Features

* Transition and emission probability matrices
* Dynamic programming implementation
* Most probable hidden state prediction
* Probability visualization using Matplotlib

### Viterbi Formula

```text id="p6qgxh"
V_t(j) = max_i (V_{t-1}(i) × a_ij × b_j(o_t))
```

---

# Technologies Used

* Python
* Tkinter
* NumPy
* Matplotlib
* Graphviz

---

# Project Structure

```text id="jlwm6t"
AI_Project/
│
├── tic_tac_toe.py
├── alpha_beta_pruning.py
├── hmm_viterbi.py
├── alpha_beta_tree.gv.png
├── hmm_probability_plot.png
├── README.md
├── requirements.txt
├── .gitignore
```

---

# How to Run the Projects

## 1. Clone the Repository

```bash id="yz7yoh"
git clone https://github.com/abhilash-20/AI_Project.git
```

## 2. Open Project Folder

```bash id="9az3ie"
cd AI_Project
```

## 3. Create Virtual Environment

```bash id="3qbb1q"
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows PowerShell

```powershell id="jlwm1k"
.\venv\Scripts\Activate.ps1
```

## 5. Install Dependencies

```bash id="jlwm0n"
pip install -r requirements.txt
```

---

# Run Individual Projects

## Tic-Tac-Toe AI

```bash id="jlwm0m"
python tic_tac_toe.py
```

## Alpha-Beta Pruning Visualization

```bash id="jlwm0l"
python alpha_beta_pruning.py
```

## Hidden Markov Model using Viterbi Algorithm

```bash id="jlwm0k"
python hmm_viterbi.py
```

---

# Screenshots

Add screenshots of:

* Tic-Tac-Toe gameplay
* Alpha-Beta pruning tree visualization
* HMM probability graph

---

# Learning Outcomes

This project helped in understanding:

* Artificial Intelligence fundamentals
* Adversarial Search
* Minimax Algorithm
* Alpha-Beta Pruning
* Hidden Markov Models
* Dynamic Programming
* Recursive Algorithms
* Probability-Based Decision Making
* Data Visualization in Python

---

# Future Improvements

Possible future enhancements:

* GUI for Alpha-Beta visualization
* Interactive HMM simulations
* Alpha-Beta optimized Tic-Tac-Toe AI
* Web-based implementation
* Multiplayer support
* Advanced AI visualizations

---

# Author

Abhilash Kashyap

---

# License

This project is created for educational and learning purposes.
