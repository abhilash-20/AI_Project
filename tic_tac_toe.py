import tkinter as tk
from tkinter import messagebox



PLAYER = "X"
AI = "O"

board = [" " for _ in range(9)]



def check_winner(brd, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for combo in win_combinations:
        if all(brd[i] == player for i in combo):
            return True

    return False



def is_draw(brd):
    return " " not in brd



def minimax(brd, depth, is_maximizing):

    # AI wins
    if check_winner(brd, AI):
        return 1

    # Player wins
    if check_winner(brd, PLAYER):
        return -1

    # Draw
    if is_draw(brd):
        return 0

    # AI turn (maximize)
    if is_maximizing:
        best_score = -float('inf')

        for i in range(9):
            if brd[i] == " ":
                brd[i] = AI
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best_score = max(score, best_score)

        return best_score

    # Player turn (minimize)
    else:
        best_score = float('inf')

        for i in range(9):
            if brd[i] == " ":
                brd[i] = PLAYER
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best_score = min(score, best_score)

        return best_score



def ai_move():
    best_score = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = AI
    buttons[move].config(text=AI, state="disabled")

    check_game_over()



def player_move(index):

    if board[index] == " ":
        board[index] = PLAYER
        buttons[index].config(text=PLAYER, state="disabled")

        if not check_game_over():
            ai_move()


def check_game_over():

    if check_winner(board, PLAYER):
        messagebox.showinfo("Game Over", "You Win!")
        disable_all_buttons()
        return True

    if check_winner(board, AI):
        messagebox.showinfo("Game Over", "AI Wins!")
        disable_all_buttons()
        return True

    if is_draw(board):
        messagebox.showinfo("Game Over", "It's a Draw!")
        return True

    return False



def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")


# RESET GAME

def reset_game():
    global board
    board = [" " for _ in range(9)]

    for btn in buttons:
        btn.config(text=" ", state="normal")



root = tk.Tk()
root.title("AI Tic Tac Toe - Minimax")

buttons = []

for i in range(9):
    btn = tk.Button(
        root,
        text=" ",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )

    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Restart Button
restart_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14),
    command=reset_game
)

restart_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()