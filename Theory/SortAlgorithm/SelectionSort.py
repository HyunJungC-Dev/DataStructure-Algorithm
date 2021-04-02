def selection_sort(x):
    for i in range(len(x)-1):
        min_idx = i
        for j in range(i+1, len(x)):
            if x[min_idx] > x[j]:
                min_idx = j
        x[min_idx], x[i] = x[i], x[min_idx]
    return x


arr = [5, 8, 1, 4, 3, 7, 2, 6, 9]
print(selection_sort(arr))
