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
        a1, b1, c1 = self.coof()
        a2, b2, c2 = other.coof()
        if a1 == 0:
            y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
            x = y
        else:
            y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
            x = -(b1 * y + c1) / a1
        return x, y

    def paralel(self, other):
        g = round(self.normal.angle1(other.normal), 6)
        return g == 0 or g == round(math.pi, 6)

    def position(self, p1, p2):
        norm = self.normal - self.p0
        vec1 = p1 - self.p0
        vec2 = p2 - self.p0
        a = norm.angle1(vec1)
        b = norm.angle1(vec2)
        if a > (math.pi / 2) and b > (math.pi / 2):
            return True
        elif a < (math.pi / 2) and b < (math.pi / 2):
            return True
        else:
            return False


class Ray:
    def __init__(self, v0, v1):
        self.v0 = v0
        self.v1 = v1

    def __repr__(self):
        return f"Ray({self.v0!r}, {self.v1!r})"

    def Contains(self, p0):
        a = p0 - self.v0
        b = self.v1 - self.v0
        if p0.x == self.v0.x and p0.y == self.v0.y:
            return True
        else:
            return a.angle1(b) == 0

    def containsOtr(r0, r1, p0):
        rh = Ray(r0, r1)
        rj = Ray(r1, r0)
        return rh.Contains(p0) and rj.Contains(p0)

    def Raydist(a, b1, c1):
        b = Line.from_points(b1, c1)
        d, y = (a - b.p0).to_base(b.normal.Dir(), b.normal.left())
        y = round(y, 10)
        if Ray.containsOtr(b1, c1, a - b.normal.Dir() * y):
            return abs(y)
        else:
            if (b1 - a).len1() < (c1 - a).len1():
                return (b1 - a).len1()
            else:
                return (c1 - a).len1()

    def Luch(a, b1, c1):
        b = Line.from_points(b1, c1)
        d, y = (a - b.p0).to_base(b.normal.Dir(), b.normal.left())
        y = round(y, 10)
        r = Ray(b1, c1)
        if r.Contains(a - b.normal.Dir() * y):
            return round(abs(y), 5)
        else:
            if (b1 - a).len1() < (c1 - a).len1():
                return (b1 - a).len1()
            else:
                return (c1 - a).len1()

    def Otrezki(a1, b1, c1, d1):
        n1 = Ray.Raydist(a1, c1, d1)
        n2 = Ray.Raydist(b1, c1, d1)
        n3 = Ray.Raydist(c1, a1, b1)
        n4 = Ray.Raydist(d1, a1, b1)
        h = Vec.is_point(a1, b1, c1, d1) and Vec.is_point(c1, d1, a1, b1)
        if h:
            return 0
        else:
            return min(n1, n2, n3, n4)


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
    text = Scanner("intersec1.in")
    a1 = text.read_line()
    b1 = text.read_line()
    with open("intersec1.out", "wt") as wrote:
        toch1 = a1.p0
        toch2 = b1.p0
        toch3 = a1.normal.left() + toch1
        toch4 = b1.normal.left() + toch2
        k = toch1 - toch3
        m = toch2 - toch4
        t1, t2 = (toch2 - toch1).to_base(k, m)
        wrote.write(f"{toch1 + k * t2}")