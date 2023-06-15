import math
EPS = 1e-9


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
        if math.atan2(self.y, self.x) < 0:
            return (math.atan2(self.y, self.x) + math.pi + math.pi)
        else:
            return math.atan2(self.y, self.x)

    # Вектор той же длины, что и self,
    # направленный перпендикулярно налево
    def left(self):
        return Vec(-self.y, self.x)

    def right(self):
        return Vec(self.y, -self.x)


class Line:
    def __init__(self, p0, normal):
        self.p0 = p0
        self.normal = normal

    def __repr__(self):
        return f"Line({self.p0!r}, {self.normal!r})"

    # 'print(line)' prints A B C
    def __str__(self):
        c = -self.p0 * self.p0
        return f"{self.normal} {c}"  # a = n.x, b = n.y

    # line = Line.from_abc(a, b, c)
    def from_abc(a, b, c):
        normal = Vec(a, b)
        p0 = normal * (-c / normal.len2())
        return Line(p0, normal)

    # line = Line.from_points(A, B)
    def from_points(A, B):
        normal = (A - B).left()
        return Line(A, normal)

    def contains(self, point):
        return abs(self.normal * (point - self.p0)) < EPS

    def coof(self):
        pass
# return self.normal.x,self.normal.y,(self.p0*self.normal.len2())/self.normal


class Scanner:
    def __init__(self, file_name):
        with open(file_name, 'rt') as input_file:
            self.__tokens = input_file.read().split()
            self.__tokens = self.__tokens[::-1]

    def read_token(self):
        return self.__tokens.pop()

    def read_float(self):
        return float(self.read_token())

    def read_vec(self):
        x = self.read_float()
        y = self.read_float()
        return Vec(x, y)

    def read_line(self):
        a = self.read_float()
        b = self.read_float()
        c = self.read_float()
        return Line.from_abc(a, b, c)


if __name__ == '__main__':
    text = Scanner("angle1.in")
    a = text.read_vec()
    b = text.read_vec()
    d = Line.from_points(a, b)
    with open("angle1.out", "wt") as wrote:
        print("oke")
        
