def quick_sort(x):
    def recursion(x, left_first_idx, right_last_idx):
        if left_first_idx >= right_last_idx:
            return

        pivot_idx = (left_first_idx+right_last_idx)//2
        curr_first_idx = left_first_idx
        curr_last_idx = right_last_idx

        # 왼쪽 정렬
        while curr_first_idx < pivot_idx:
            if x[curr_first_idx] > x[pivot_idx]:
                tmp = x[curr_first_idx]
                for i in range(curr_first_idx+1, right_last_idx+1):
                    x[i-1] = x[i]  # 앞으로 땡김
                pivot_idx -= 1
                x[right_last_idx] = tmp
            else:
                curr_first_idx += 1
        # 오른쪽 정렬
        while pivot_idx < curr_last_idx:
            if x[curr_last_idx] < x[pivot_idx]:
                tmp = x[curr_last_idx]
                for i in range(curr_last_idx, left_first_idx, -1):
                    x[i] = x[i-1]  # 뒤로 밈
                pivot_idx += 1
                x[left_first_idx] = tmp
            else:
                curr_last_idx -= 1
        recursion(x, left_first_idx, pivot_idx-1)
        recursion(x, pivot_idx+1, right_last_idx)
    recursion(x, 0, len(x)-1)


arr = [8, 6, 2, 1, 4, 7, 5, 3]
quick_sort(arr)
print(arr)
