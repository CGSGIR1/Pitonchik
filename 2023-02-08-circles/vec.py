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
        if isinstance(a, Vec):
            return self.x * a.x + self.y * a.y
        return Vec(round(self.x * a, 10), round(self.y * a, 10))

    # Квадрат длины вектора
    def len2(self):
        return (self.x ** 2 + self.y ** 2)

    def len1(self):
        return self.len2() ** 0.5

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
            return round(abs(self.angle() - other.angle()), 10)

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
        ang = math.sin(self.angle() - other.angle())
        return self.len1() * other.len1() * ang

    def to_base(self, v, u):
        cp = u % v
        return round((self % v) / cp, 9), round(u % self / cp, 9)

    def is_point(a, b, c, d):
        cp1 = (b - a) % (c - a)
        cp2 = (b - a) % (d - a)
        cp3 = (d - c) % (a - c)
        cp4 = (d - c) % (b - c)
        if cp1 == 0 and cp2 == 0 and cp1 == 0 and cp2 == 0:
            g = (c - b).angle1(d - b)
            o = (c - a).angle1(d - a)
            return g + o == math.pi
        else:
            return sign(cp1) * sign(cp2) <= 0
