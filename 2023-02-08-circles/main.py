import random
import keyboard
import math
import tkinter as tk
import time
import tkinter.ttk as ttk
from math import cos, sin
from vec import Vec
from point import MovePoint
from line import Line
from pointsSort import quick_sort_point
from circle import Circle
from intersection import Intersection

def point_side(line_start, line_end, point):
    line_vec = line_end - line_start
    point_vec = point - line_start

    # Рассчитываем векторное произведение двух векторов
    cross_product = line_vec.x * point_vec.y - line_vec.y * point_vec.x

    if cross_product > 0:
        return False
    elif cross_product < 0:
        return True
    else:
        return True


def newAngle(line_start, line_end, point):
    # Вычисляем координаты векторов между началом отрезка, его концом и исходной точкой
    line_vector = line_end - point
    point_vector = line_start - point

    # Вычисляем длины векторов
    line_length = math.sqrt(line_vector.x ** 2 + line_vector.y ** 2)
    point_length = math.sqrt(point_vector.x ** 2 + point_vector.y ** 2)

    # Вычисляем скалярное произведение векторов
    dot_product = line_vector.x * point_vector.x + line_vector.y * point_vector.y

    # Вычисляем косинус угла между векторами
    a = line_length * point_length
    if a == 0:
        a = 10 ** 10
    cos_angle = dot_product / a
    angle_rad = math.acos(cos_angle)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def _Triangularion(Points):
    global c
    # сортируем точки по координате x
    quick_sort_point(Points)
    print(len(Points))
    delPoints = []
    # ищем одинаковые точки
    for i in range(len(Points)):
        for j in range(i + 1, len(Points)):
            if Points[i].x == Points[j].x:
                if Points[i].y == Points[j].y:
                    delPoints.append(j)
                    i = j
            else:
                i += 1
    newPoints = []
    k = 0
    # создаем новый массив без повторяющихся точек
    if len(delPoints) > 0:
        for i in range(len(Points)):
            if i != delPoints[k]:
                newPoints.append(Points[i])
            else:
                if k < len(delPoints) - 1:
                    k += 1
    else:
        for i in range(len(Points)):
            newPoints.append(Points[i])

    # ищем самую левую нижнию точку
    lenPoints = len(newPoints)
    print(lenPoints)
    P0 = 0
    for i in range(lenPoints):
        if newPoints[i].x != newPoints[P0].x:
            break
        if newPoints[i].y < newPoints[P0].y:
            P0 = i
    c.itemconfig(newPoints[P0]._id, fill='yellow')

    # ищем вторую точку для первого ребра
    secondPoints = []
    for i in range(lenPoints):
        correct = True
        if i == P0:
            continue
        for j in range(lenPoints):
            if i == j or j == P0:
                continue
            if not point_side(newPoints[P0], newPoints[i], newPoints[j]):
                correct = False
                break
        if correct == True:
            secondPoints.append(i)
    P1 = secondPoints[0]
    dist = newPoints[P0].lenTwoPoints(newPoints[P1])
    print(dist)
    for i in range(len(secondPoints)):
        distNew = newPoints[P0].lenTwoPoints(newPoints[secondPoints[i]])
        if dist > distNew:
            dist = distNew
            P1 = secondPoints[i]

    ActiveEdges = [[P0, P1]]
    itogEdges = [[P0, P1]]
    ActiveLines = [Line(c, newPoints[P0], newPoints[P1], "red")]
    SleepLines = []
    print(ActiveEdges.count([P0, P1]))
    while len(ActiveEdges) != 0:
        time.sleep(0.1)
        n = len(ActiveEdges) - 1
        angle = 0
        anglem = 0
        P2 = None
        P3 = None
        P0 = ActiveEdges[n][0]
        P1 = ActiveEdges[n][1]
        for i in range(lenPoints):
            if i == ActiveEdges[n][0] or i == ActiveEdges[n][1]:
                continue
            print(P0, P1, i)
            angle2 = newAngle(newPoints[P0], newPoints[P1], newPoints[i])
            if point_side(newPoints[P0], newPoints[P1], newPoints[i]):
                if angle2 > angle:
                    P2 = i
                    angle = angle2
            else:
                if angle2 > anglem:
                    P3 = i
                    anglem = angle2
        ActiveEdges.pop()
        del ActiveLines[-1]
        SleepLines.append(Line(c, newPoints[P0], newPoints[P1], "black"))
        if P2 != None:
            if itogEdges.count([P0, P2]) == 0 and itogEdges.count([P2, P0]) == 0:
                ActiveEdges.append([P2, P0])
                ActiveLines.append(Line(c, newPoints[P2], newPoints[P0], "red"))
                itogEdges.append([P2, P0])
            if itogEdges.count([P1, P2]) == 0 and itogEdges.count([P2, P1]) == 0:
                ActiveEdges.append([P2, P1])
                itogEdges.append([P2, P1])
                ActiveLines.append(Line(c, newPoints[P2], newPoints[P1], "red"))
        if P3 != None and P2 != P3:
            if itogEdges.count([P0, P3]) == 0 and itogEdges.count([P3, P0]) == 0:
                ActiveEdges.append([P3, P0])
                itogEdges.append([P3, P0])
                ActiveLines.append(Line(c, newPoints[P3], newPoints[P0], "red"))
            if itogEdges.count([P1, P3]) == 0 and itogEdges.count([P3, P1]) == 0:
                ActiveEdges.append([P3, P1])
                itogEdges.append([P3, P1])
                ActiveLines.append(Line(c, newPoints[P3], newPoints[P1], "red"))


def Triangularion():
    global points
    _Triangularion(points)
def addPoint(ev):
    global c, flag, points
    if flag == True:
        k = MovePoint(c, (ev.x, ev.y))
        points.append(k)
        if (len(points) > 1):
            for i in range(len(points) - 1):
                pass
                #Line(c, points[i], k)

def FlagPoint():
    global flag, points
    if flag == True:
        flag = False
    else:
        flag = True

def DeletePoints():
    global points
    if (len(points) > 1):
        points[-1].deletePoint()
        points.pop()

def ClearTriangl():
    global points
    print(":(")
    for i in range(len(points)):
        points[i].deleteLine()

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        global c, points
        points = []
        super().__init__(*args, **kwargs)
        self.title("Geometry visalustion")
        self.geometry("1000x800")

        c = tk.Canvas(self, bg="white", bd=0, highlightthickness=0)
        c.pack(anchor=tk.NW, fill=tk.BOTH, expand=True, padx=5, pady=5)

        keyboard.add_hotkey("z", FlagPoint)
        keyboard.add_hotkey("d", DeletePoints)
        keyboard.add_hotkey("t", Triangularion)
        keyboard.add_hotkey("c", ClearTriangl)
        c.bind("<Button-1>", addPoint)
        # p0 = Point(c, (100, 200))
        #line1 = Line(c, MovePoint(c, (100, 200)),
        #             MovePoint(c, (800, 600)))
        #line2 = Line(c, MovePoint(c, (500, 100)),
        #             MovePoint(c, (100, 400)))
        #circle1 = Circle(c, MovePoint(c, (300, 100)),
        #                 MovePoint(c, (200, 400)))
        #circle2 = Circle(c, MovePoint(c, (400, 500)),
        #                 MovePoint(c, (600, 700)))
        #inter1 = Intersection(c, line1, line2)
        #inter2 = Intersection(c, circle1, line1)
        #inter3 = Intersection(c, circle1, circle2)
        c.tag_raise("point")

if __name__ == '__main__':
    global flag
    flag = True
    win = Window()
    win.mainloop()
