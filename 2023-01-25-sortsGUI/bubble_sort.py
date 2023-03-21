def bubble_sort(a):
    n = len(a)
    for k in range(n - 1):
        for j in range(n - 1 - k):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
    return a