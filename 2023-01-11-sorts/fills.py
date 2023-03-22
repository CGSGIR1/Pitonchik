import random

def fill_increase(n):
    return list(range(n))


def fill_decrease(n):
    a = list(range(n))
    a.reverse()
    return a


def fill_random(n):
    a = fill_increase(n)
    random.shuffle(a)
    return a


def fill_almostsort(n):
    a = fill_increase(n)
    a[-1], a[0] = a[0], a[-1]
    return a
