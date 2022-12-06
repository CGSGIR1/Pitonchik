# Родин Илья heap_sort
import random
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
    k = math.ceil(math.log2(n))
    for v in range(k // 2 - 1, -1, -1):
        heapify(a, n, v)


def heap_sort(a, n):
    build_heap(a, n)
    while n > 1:
        n -= 1
        a[n], a[0] = a[0], a[n]
        heapify(a, n, 0)
        

if __name__ == '__main__':
    a = input()
    b = list(map(int, input().split()))
    heap_sort(b, len(b))
    print(*b)