
def merge_sort(x, first=0, last=-1, arr=None):
    if last == -1:
        last = len(x)-1
    if arr is None:
        arr = [0]*len(x)
    if first >= last:  # 같으면 길이가 1인 것 = 길이가 1일때까지 반으로 쪼갠다.
        return

    mid = (first+last)//2
    merge_sort(x, first, mid, arr)
    merge_sort(x, mid+1, last, arr)
    i, j = first, mid+1
    for k in range(first, last+1):
        if j > last:
            arr[k] = x[i]
            i += 1
        elif i > mid:
            arr[k] = x[j]
            j += 1
        elif x[i] <= x[j]:
            arr[k] = x[i]
            i += 1
        else:  # j가 더 작은 것
            arr[k] = x[j]
            j += 1
    x[first:last+1] = arr[first:last+1]


x = [5, 25, 6, 2, 3, 7]
merge_sort(x, 0, len(x)-1, [0]*len(x))
print(x)
