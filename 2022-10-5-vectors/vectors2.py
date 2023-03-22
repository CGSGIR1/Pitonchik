import math
EPS = 1e-9


def sign(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1


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

    def angle1(self, other):
        if abs(self.angle() - other.angle()) > math.pi:
            return 2 * math.pi - abs(self.angle() - other.angle())
        else:
            return abs(self.angle() - other.angle())

    # Вектор той же длины, что и self,
    # направленный перпендикулярно налево
    def left(self):
        return Vec(-self.y, self.x)

    def right(self):
        return Vec(self.y, -self.x)

    def Dir(self):
        return self * (1 / self.len1())

    def bis(self, v2, x):
        a = self.Dir()
        b = v2.Dir()
        c = a + b
        norm = c.right()
        return Line(x, norm).coof()

    def __mod__(self, other):
        if self.len1() == 0 or other.len1() == 0:
            return 0
        ang = math.sin(self.angle1(other))
        return self.len1() * other.len1() * ang

    def to_base(self, v, u):
        cp = u % v
        return (self % v) / cp, u % self / cp

    def is_point(c, d, a, b):
        cp1 = (b - a) % (c - a)
        cp2 = (b - a) % (d - a)
        return sign(cp1) * sign(cp2) <= 0


class Line:
    def __init__(self, p0, normal):
        self.p0 = p0
        self.normal = normal

    def __repr__(self):
        return f"Line({self.p0!r}, {self.normal!r})"

    # 'print(line)' prints A B C
    def __str__(self):
        c = self.p0 * self.p0
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
        a = self.normal.x
        b = self.normal.y
        return a, b, -(a * self.p0.x + b * self.p0.y)

    def parLine(self, R):
        r = self.normal.Dir() * R
        a = Line(self.p0 + r, self.normal)
        b = Line(self.p0 + (r * (-1)), self.normal)
        return a.coof(), b.coof()

    def intersec(self, other):
        pass


class Ray:
    def __init__(self, v0, v1):
        self.v0 = v0
        self.v1 = v1

    def __repr__(self):
        return f"Ray({self.v0!r}, {self.v1!r})"

    def NotContains(self, p0):
        a = Vec(p0.x - self.v0.x, p0.y - self.v0.y)
        b = Vec(self.v1.x - self.v0.x, self.v1.y - self.v0.y)
        if p0.x == self.v0.x and p0.y == self.v0.y:
            return False
        else:
            return a * b < 0 or a.angle1(b) != 0


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
    text = Scanner("intersec2.in")
    a = text.read_vec()
    b = text.read_vec()
    c = text.read_vec()
    d = text.read_vec()
    with open("intersec2.out", "wt") as wrote:
        t1 = not (Vec.is_point(c, d, a, b) or Vec.is_point(a, b, c, d))
        if t1:
            wrote.write(f"YES")
        else:
            wrote.write(f"NO")
