import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("300x300")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[tk.Button(self, text="", width=30, height=14, command=lambda row=row, col=col: self.on_button_click(row, col)) for col in range(3)] for row in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
            return True
        # Check diagonals
        if (row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player) or \
           (row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
