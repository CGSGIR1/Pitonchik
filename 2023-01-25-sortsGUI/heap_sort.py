# Родин Илья heap_sort
import math


def heapify(a, n, v):
    root = v
    left = 2 * v + 1
    right = 2 * v + 2
    if left < n and a[root] < a[left]:
        root = left
    if right < n and a[root] < a[right]:
        root = right
    if root != v:
        a[v], a[root] = a[root], a[v]
        heapify(a, n, root)


def build_heap(a, n):
    for v in range(n // 2 - 1, -1, -1):
        heapify(a, n, v)


def _heap_sort(a, n):
    build_heap(a, n)
    while n > 1:
        n -= 1
        a[n], a[0] = a[0], a[n]
        heapify(a, n, 0)


def heap_sort(a):
    _heap_sort(a, len(a))
    return a
