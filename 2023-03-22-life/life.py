#Rodin Ilya 9-1 game life
import random
import tkinter as tk


class Window(tk.Tk):
    CELL_SIZE = 10
    GRID_W = 50
    GRID_H = 30
    BORDER = 1
    COLOR_BACK = "#CCCCCC"
    COLOR_ALIVE = "limegreen"
    COLOR_DEAD = "#888888"
    FRAME_DELAY = 200
    
    def __init__(self):
        super().__init__()
        self.title("Life game")
        self.button_init = tk.Button(text="Init game", command=self.game_init)
        self.button_init.pack()

        cs, w, h = self.CELL_SIZE, self.GRID_W, self.GRID_H
        c = self.canvas = tk.Canvas(self, width=cs * w, height=cs * h)
        self.canvas.pack()
        
        self.grid = [[0] * w for y in range(h)]
        for y in range(h):
            for x in range(w):
                self.grid[y][x] = c.create_rectangle(cs * x, cs * y, cs * (x + 1), cs * (y + 1), fill = self.COLOR_BACK)
        self.next_frame()  # Запускаем рисовку кадров раз в 1/5 секунды

    def cell_color(self, x, y, color):
        self.canvas.itemconfig(self.grid[y][x], fill=color)
    
    def cell_get(self, x, y):
        prop = self.canvas.itemconfig(self.grid[y][x])
        c = prop["fill"][4]
        return c == self.COLOR_ALIVE

    def cell_set(self, x, y, is_alive):
        if is_alive:
            c = self.COLOR_ALIVE
        else:
            c = self.COLOR_DEAD
        self.cell_color(x, y, c)

    def game_init(self):
        for y in range(self.GRID_H):
            for x in range(self.GRID_W):
                self.cell_set(x, y, random.random() < 0.5)
    
    def next_frame(self):
        # Запоминаем, кто жив, кто мёртв
        frame = [[0] * self.GRID_W for y in range(self.GRID_H)]
        for y in range(self.GRID_H):
            for x in range(self.GRID_W):
                frame[y][x] = self.cell_get(x, y)

        # Строим новый кадр
        for y in range(0, self.GRID_H):
            for x in range(0, self.GRID_W):
                cnt = 0
                for x1 in range(-1, 2):
                    for y1 in range(-1, 2):
                        if  0 <= x + x1 < self.GRID_W and 0 <= y + y1 < self.GRID_H:
                            if frame[y + y1][x + x1] == 1:
                                if x1 != 0 and y1 != 0:
                                    cnt += 1
                if cnt == 2 and frame[y][x] != 1:
                    self.cell_set(x, y, 1)
                elif (cnt == 2 or cnt == 3) and frame[y][x] == 1:
                    self.cell_set(x, y, 1)
                else:
                    self.cell_set(x, y, 0)
                #... Считаем соседей, закрашиваем клетки
                #self.cell_set(x, y, ???)
        self.after(self.FRAME_DELAY, self.next_frame)

    
if __name__ == "__main__":
    win = Window()
    win.mainloop()
