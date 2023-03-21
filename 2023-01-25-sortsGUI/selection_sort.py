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