import random
import tkinter as tk 
import tkinter.ttk as ttk
from math import cos, sin
from vec import Vec
from point import MovePoint
from line import Line
from circle import Circle
from intersection import Intersection

class Window(tk.Tk):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Geometry visalustion")
        self.geometry("1000x800")

        c = tk.Canvas(self, bg="white", bd=0, highlightthickness=0)
        c.pack(anchor=tk.NW, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # p0 = Point(c, (100, 200))
        line1 = Line(c, MovePoint(c, (100, 200)),
                     MovePoint(c, (800, 600)))
        line2 = Line(c, MovePoint(c, (500, 100)),
                     MovePoint(c, (100, 400)))
        circle1 = Circle(c, MovePoint(c, (300, 100)),
                     MovePoint(c, (200, 400)))
        circle2 = Circle(c, MovePoint(c, (400, 500)),
                     MovePoint(c, (600, 700)))
        inter1 = Intersection(c, line1, line2)
        inter2 = Intersection(c, circle1, line1)
        inter3 = Intersection(c, circle1, circle2)
        c.tag_raise("point")


if __name__ == '__main__':
    win = Window()
    win.mainloop()
