import random


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        x = a[i]
        j = i
        while j > 0 and a[j - 1] >= x:
            a[j] = a[j - 1]
            j -= 1
        a[j] = x
    return a


def searchMin(k, a):
    c = k
    for i in range(k, len(a)):
        if a[i] < a[c]:
            c = i
    return c


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        j = searchMin(i, a)
        a[i], a[j] = a[j], a[i]
    return a


def bubble_sort(a):
    n = len(a)
    for k in range(n - 1):
        for j in range(n - 1 - k):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
    return a


def quick_sort(a, f, last):
    if last - f == 0:
        return a
    i, j = partion(a, f, last)
    quick_sort(a, f, i)
    quick_sort(a, j, last)
    return a


def partion(a, f, last):
    x = a[random.randrange(f, last)]
    i = f
    for k in range(f, last):
        if a[k] < x:
            a[i], a[k] = a[k], a[i]
            i += 1
    j = i
    for k in range(i, last):
        if a[k] == x:
            a[j], a[k] = a[k], a[j]
            j += 1
    return i, j


b = list(map(int, input().split()))
print(' '.join(list(map(str, (quick_sort(b, 0, len(b)))))))