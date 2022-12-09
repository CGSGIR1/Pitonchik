def merge(a, first, medium, last):
    res = []
    i = first
    j = medium
    for k in range(last - first):
        if j == last or (a[i] <= a[j] and i < medium):
            res.append(a[i])
            i += 1
        else:
            res.append(a[j])
            j += 1
    a[first:last] = res


def merge_sort(a, first, last):
    medium = (first + last) // 2
    if last - first <= 2:
        merge(a, first, medium, last)
        return
    merge_sort(a, first, medium )
    merge_sort(a, medium, last)
    merge(a, first, medium, last)
    
a = [1, 5, 2, 9, 4, 23, 1, 5, 6]
merge_sort(a, 0, len(a))
print(*a)