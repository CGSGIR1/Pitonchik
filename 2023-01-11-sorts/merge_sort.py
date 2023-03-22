# Родин Илья
def merge(a, first, medium, last):
    res = []
    i = first
    j = medium
    for k in range(last - first):
        if j == last or (i < medium and a[i] <= a[j]):
            res.append(a[i])
            i += 1
        else:
            res.append(a[j])
            j += 1
    a[first:last] = res


def _merge_sort(a, first, last):
    medium = (first + last) // 2
    if last - first <= 2:
        merge(a, first, medium, last)
        return
    _merge_sort(a, first, medium)
    _merge_sort(a, medium, last)
    merge(a, first, medium, last)


def merge_sort(a):
    _merge_sort(a, 0, len(a))
