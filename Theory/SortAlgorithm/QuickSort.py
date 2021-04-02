def quick_sort(x):
    if len(x) < 2:
        return x

    left = []
    right = []
    equl = []
    pivot = x[len(x)//2]
    for el in x:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            equl.append(el)
    return quick_sort(left) + equl + quick_sort(right)


arr = [7, 13, 3, 9, 1, 12, 2, 14, 6, 11, 3, 5, 8, 10, 15]
print(quick_sort(arr))
