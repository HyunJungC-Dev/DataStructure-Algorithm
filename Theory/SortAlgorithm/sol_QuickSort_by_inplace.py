def quicksort(x):
    def partition(low, high):
        pivot = x[(low+high)//2]
        while low <= high:
            while x[low] < pivot:
                low += 1
            while x[high] > pivot:
                high -= 1
            if low <= high:
                x[low], x[high] = x[high], x[low]
                low += 1
                high -= 1
        return low

    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)
    sort(0, len(x)-1)
    return x


arr = [7, 13, 3, 9, 1, 12, 2, 14, 6, 11, 3, 5, 8, 10, 15]
print(quicksort(arr))
