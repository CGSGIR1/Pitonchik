import math
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
         
    def __repr__(self):
        return f"Vec({self.x!r}, {self.y!r})"
 
    def __str__(self):
        return f"{self.x} {self.y}"
 
    # -v
    def __neg__(self):
        return Vec(-self.x, -self.y)
 
    # a + b
    def __add__(self, v):
        return Vec(self.x + v.x, self.y + v.y)
 
    # a - b
    def __sub__(self, v):
        return Vec(self.x - v.x, self.y - v.y)
 
    # Скалярное произведение (dot product)
    # или умножение вектора на число, если a — не вектор
    def __mul__(self, a):
        if type(a) is Vec:
            return self.x * a.x + self.y * a.y
        return Vec(self.x * a, self.y * a)
 
    # Квадрат длины вектора
    def len2(self):
        return (self.x ** 2 + self.y ** 2)
 
    def len1(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
 
    # Полярный угол (угол к оси OX) в диапазоне (-pi, pi]
    def angle(self):
        return math.atan2(self.y, self.x)
 
    # Вектор той же длины, что и self,
    # направленный перпендикулярно налево
    def left(self):
        return Vec(-self.y, self.x)
 
    def right(self):
        return Vec(self.y, -self.x)
if __name__ == '__main__':
    vec1 = Vec(3,3)
    vec2 = Vec(0,1)
    print(vec1.len2())
    print(vec1.left())
    print(vec1.right())
 