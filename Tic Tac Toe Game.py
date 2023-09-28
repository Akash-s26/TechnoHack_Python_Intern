import tkinter as tk
from tkinter import messagebox

class TicTacToe:

    def __init__(self, root):
        self.root = root

        self.root.title("Tic Tac Toe")

        # Initialize variables
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        # Create buttons
        self.buttons = [tk.Button(root, text=" ", font=('normal', 24), width=5, height=2,
                                  command=lambda i=i: self.on_click(i)) for i in range(9)]

        # Place buttons on grid
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

        # Create label to display winner
        self.winner_label = tk.Label(root, text="", font=('normal', 20))
        self.winner_label.grid(row=3, columnspan=3)

    def on_click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                winner_message = f"Player {self.current_player} wins!"
                self.winner_label.config(text=winner_message)
                messagebox.showinfo("Game Over", winner_message)
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):


        # Check rows, columns, and diagonals for a win
        for i in range(0, 9, 3):  # Check rows
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return True
        for i in range(3):  # Check columns
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ")
        self.current_player = "X"
        self.winner_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)

    
    root.mainloop()
