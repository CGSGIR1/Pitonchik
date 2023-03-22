import tkinter as tk
import random

def toggle(a):
    a.red = not a.red
    if a.red:
        a.config(bg="red")
    else:
        a.config(bg="blue")

def pressed(b, x1, y1):
    for x in range(W):
        for y in range(H):
            if x == x1 or y == y1:
                toggle(buttons[x][y])
    Check()

def NewGame():
    for x in range(W):
        for y in range(H):
            buttons[x][y].red = bool(random.getrandbits(1))
            toggle(buttons[x][y])

def Check():
    color = buttons[0][0].red
    win = True
    for x in range(W):
        for y in range(H):
            if buttons[x][y].red != color:
                win = False
    if win:
        result = tk.messagebox.askyesno(title="You win!", message="You win! Restart?")
        if result:
            NewGame()
        else:
            tk.destroy()
            

window = tk.Tk()
window.geometry("600x330")
window.title("Flip Game")
window.defaultFont = tk.font.nametofont("TkDefaultFont")
window.defaultFont.configure( family = "Comic Sans MS", 
                                 size = 20, 
                                 weight = "bold")
lbl = tk.Label(window, text="Super Game")
lbl.pack()

W, H = 4, 4
buttons = [[0] * H for i in range(W)]
colors = [[0] * H for i in range(W)]
for x in range(W):
    row = tk.Frame(window)
    for y in range(H):        
        button = tk.Button(row, width=3, text="-")
        button.config(command = lambda a=button, b=x, c=y : pressed(a, b, c))
        buttons[x][y] = button
        button.red = False
        button.pack(side=tk.LEFT)
    row.pack()
NewGame()


window.mainloop()