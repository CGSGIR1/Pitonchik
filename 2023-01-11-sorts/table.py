# Илья Родин 11.01.2023

from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
import random 
import time
from fills import *

n = 10 ** 5
sorts = [(bubble_sort, "bubble"), (insertion_sort, "insertion"), (selection_sort, "selection"),
        (heap_sort, "heap"), (quick_sort, "quick"), (merge_sort, "merge")]
fills = [(fill_increase, "increase"), (fill_decrease, "decrease"),
         (fill_random, "random"), (fill_almostsort, "almostsort")]
print("               ", end = "")
for sortk, name in sorts:
    print(f"{name:10}", end = "")
print()
i = 0
for fill, name in fills:
    print(f"{name:10}", end = "")
    for sort, sort_name in sorts:
        if n >= 10**4 and i < 3:
            print("      skip", end = "")
        else:
            a = fill(n)
            correct = sorted(a)
            start = time.time()
            sort(a)
            delta = time.time() - start
            if a == correct:
                print(f"{delta:10.3f}", end = "")
            else:
                print("f{Fail:10}", end = "")
        i += 1
    i = 0
    print()
