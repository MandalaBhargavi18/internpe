import tkinter as tk
import random

class SnakeGame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Snake Game")
        self.geometry("400x400")
        
        self.canvas = tk.Canvas(self, bg="black", width=1500, height=1000)
        self.canvas.pack()
        
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.spawn_food()
        self.direction = "Right"
        
        self.bind("<KeyPress>", self.change_direction)
        
        self.move_snake()
    
    def spawn_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                return (x, y)
    
    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="green", tag="snake")
    
    def draw_food(self):
        self.canvas.delete("food")
        x, y = self.food
        self.canvas.create_rectangle(x, y, x+20, y+20, fill="red", tag="food")
    
    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym
    
    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 20)
        elif self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 20, head[1])
        
        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.food = self.spawn_food()
        else:
            self.snake.pop()
            self.snake.insert(0, new_head)
        
        if (new_head in self.snake[1:] or 
            new_head[0] < 0 or new_head[0] >= 400 or 
            new_head[1] < 0 or new_head[1] >= 400):
            self.game_over()
        else:
            self.draw_snake()
            self.draw_food()
            self.after(100, self.move_snake)
    
    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 200, text="Game Over!", fill="white", font=("Arial", 20))

if __name__ == "__main__":
    app = SnakeGame()
    app.mainloop()
