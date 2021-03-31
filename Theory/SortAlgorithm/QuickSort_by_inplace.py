def quick_sort(x):
    def recursion(x, left_first_idx, right_last_idx):
        if left_first_idx >= right_last_idx:  # 탈출 조건 = 가장 작은 경우
            return

        pivot_idx = (left_first_idx+right_last_idx)//2
        bias_left_idx = left_first_idx
        bias_right_idx = right_last_idx

        # 왼쪽 정렬
        while bias_left_idx < pivot_idx:
            if x[bias_left_idx] > x[pivot_idx]:
                tmp = x[bias_left_idx]
                for i in range(bias_left_idx+1, right_last_idx+1):
                    x[i-1] = x[i]  # 앞으로 땡김
                pivot_idx -= 1
                x[right_last_idx] = tmp
            else:
                bias_left_idx += 1
        # 오른쪽 정렬
        while pivot_idx < bias_right_idx:
            if x[bias_right_idx] < x[pivot_idx]:
                tmp = x[bias_right_idx]
                for i in range(bias_right_idx, left_first_idx, -1):
                    x[i] = x[i-1]  # 뒤로 밈
                pivot_idx += 1
                x[left_first_idx] = tmp
            else:
                bias_right_idx -= 1
        recursion(x, left_first_idx, pivot_idx-1)
        recursion(x, pivot_idx+1, right_last_idx)
    recursion(x, 0, len(x)-1)


arr = [8, 6, 2, 1, 4, 7, 5, 3]
quick_sort(arr)
print(arr)
arr = [14, 11, 9, 8, 6, 15, 10, 2, 13, 1, 4, 11, 7, 5, 12, 3]
quick_sort(arr)
print(arr)
