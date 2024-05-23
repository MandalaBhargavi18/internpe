import tkinter as tk

# Constants
ROWS = 6
COLUMNS = 7
PLAYER1 = 1
PLAYER2 = 2

class ConnectFour:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")
        self.canvas = tk.Canvas(self.root, width=COLUMNS*60, height=ROWS*60)
        self.canvas.pack()
        self.board = [[0] * COLUMNS for _ in range(ROWS)]
        self.turn = PLAYER1
        self.draw_board()
        self.canvas.bind("<Button-1>", self.drop_piece)
        self.game_over = False

    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                self.canvas.create_rectangle(col*60, row*60, (col+1)*60, (row+1)*60, fill="blue")
                if self.board[row][col] == PLAYER1:
                    self.canvas.create_oval(col*60+5, row*60+5, (col+1)*60-5, (row+1)*60-5, fill="red")
                elif self.board[row][col] == PLAYER2:
                    self.canvas.create_oval(col*60+5, row*60+5, (col+1)*60-5, (row+1)*60-5, fill="yellow")

    def drop_piece(self, event):
        if not self.game_over:
            col = event.x // 60
            if self.is_valid_location(col):
                row = self.get_next_open_row(col)
                self.drop_piece_on_board(row, col)
                if self.winning_move(row, col):
                    self.game_over = True
                    winner = "Player 1" if self.turn == PLAYER1 else "Player 2"
                    self.canvas.create_text(COLUMNS*30, ROWS*30, text=f"{winner} wins!", font=("Helvetica", 24))
                elif self.is_board_full():
                    self.game_over = True
                    self.canvas.create_text(COLUMNS*30, ROWS*30, text="It's a tie!", font=("Helvetica", 24))
                else:
                    self.switch_turn()

    def is_valid_location(self, col):
        return self.board[ROWS-1][col] == 0

    def get_next_open_row(self, col):
        for r in range(ROWS):
            if self.board[r][col] == 0:
                return r

    def drop_piece_on_board(self, row, col):
        self.board[row][col] = self.turn
        self.draw_board()

    def winning_move(self, row, col):
        # Check horizontal
        for c in range(COLUMNS-3):
            if self.board[row][c] == self.turn and self.board[row][c+1] == self.turn and self.board[row][c+2] == self.turn and self.board[row][c+3] == self.turn:
                return True
        # Check vertical
        for r in range(ROWS-3):
            if self.board[r][col] == self.turn and self.board[r+1][col] == self.turn and self.board[r+2][col] == self.turn and self.board[r+3][col] == self.turn:
                return True
        # Check positive slope diagonal
        for c in range(COLUMNS-3):
            for r in range(ROWS-3):
                if self.board[r][c] == self.turn and self.board[r+1][c+1] == self.turn and self.board[r+2][c+2] == self.turn and self.board[r+3][c+3] == self.turn:
                    return True
        # Check negative slope diagonal
        for c in range(COLUMNS-3):
            for r in range(3, ROWS):
                if self.board[r][c] == self.turn and self.board[r-1][c+1] == self.turn and self.board[r-2][c+2] == self.turn and self.board[r-3][c+3] == self.turn:
                    return True
        return False

    def is_board_full(self):
        return all(self.board[0])

    def switch_turn(self):
        self.turn = PLAYER1 if self.turn == PLAYER2 else PLAYER2

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = ConnectFour()
    game.run()
