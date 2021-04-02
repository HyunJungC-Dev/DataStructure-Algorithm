def merge_sort(x, first=0, last=-1, arr=None):
    if last == -1:
        last = len(x)-1
    if arr is None:
        arr = [0]*len(x)
    # 종료 조건
    if first >= last:  # 같으면 길이가 1인 것 = 길이가 1일때까지 반으로 쪼갠다.
        return

    # recursion 부분
    mid = (first+last)//2
    merge_sort(x, first, mid, arr)
    merge_sort(x, mid+1, last, arr)

    # 왼쪽과 오른쪽 Merge 부분
    i, j = first, mid+1  # 왼쪽 시작idx와 오른쪽 시작 idx
    for k in range(first, last+1):
        if j > last:  # 오른쪽에 더이상 붙일 것이 없다.
            arr[k] = x[i]  # 남은 왼쪽을 붙임
            i += 1
        elif i > mid:  # 왼쪽 것이 더이상 붙일 것이 없다.
            arr[k] = x[j]  # 남은 오른쪽 붙임
            j += 1
        # 왼쪽 맨 앞 과 오른쪽 맨 앞, 둘 중 더 작은 것을 골라 붙임
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
