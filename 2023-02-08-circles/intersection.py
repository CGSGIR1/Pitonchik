from shape import Shape
from line import Line
from circle import Circle
from point import Point
from vec import Vec
import random


class Intersection(Shape):
    def __init__(self, canvas, sh1, sh2):
        super().__init__(canvas)
        for s in sh1, sh2:
            s.add_dependency(self)
        self.sh1, self.sh2 = sh1, sh2
        self.redraw()

    def redraw(self):
        if type(self.sh1) is Line and type(self.sh2) is Line:
            self.intersectLL(self.sh1, self.sh2)
        if type(self.sh1) is Circle and type(self.sh2) is Line:
            self.intersectCL(self.sh1, self.sh2)
        for p in self._points:
            p.redraw()
    
    def intersectCL(self, circle1, line1):
        self._points = []
        center = circle1.C
        P = circle1.P
        A = line1.p0
        B = line1.p1
        n = (A - B).left()
        n = n.Dir()
        u = n.right()
        u = u.Dir()
        rad = Vec.len1(center - P)
        x = (A - center) * n
        if rad ** 2 - x ** 2 >= 0:
            y = (rad ** 2 - x ** 2) ** 0.5
            self._points.append(Point(self._c, (center.x + x + y, center.y + y), "blue"))
            self._points.append(Point(self._c, (center.x - x, center.y - y), "blue"))
            self._points.append(Point(self._c, (center.x + x, center.y - y), "blue"))
            self._points.append(Point(self._c, (center.x - x, center.y + y), "blue"))

    def intersectLL(self, line1, line2):
        self._points = []
        toch1 = line1.p0
        toch2  = line2.p0
        B1 = line1.p1
        B2 = line2.p1
        normal1 = (toch1 - B1).left()
        normal2 = (toch2 - B2).left()
        toch3 = normal1.left() + toch1
        toch4 = normal2.left() + toch2
        k = toch1 - toch3
        m = toch2 - toch4
        t1, t2 = (toch2 - toch1).to_base(k, m)
        fin = toch1 + k * t2
        self._points.append(Point(self._c, (fin.x, fin.y), "blue"))