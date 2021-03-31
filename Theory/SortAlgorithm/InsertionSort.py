def insert_sort(x):
    for i in range(1, len(x)):
        j = i-1  # j range(0, len(x)-1)
        # x[0]는 맨 처음 정렬된 상태로 본다.
        key = x[i]  # key는 정렬되지 않은 영역 x[1]부터 순서대로 뽑은 것
        while x[j] > key and j >= 0:  # 현재 정렬된 곳에서 key의 위치를 찾는다.
            # 정렬된 영역의 x[j]가 key보다 클때까지 계속 이동한다.
            x[j+1] = x[j]  # x[j]
            j = j-1
        x[j+1] = key
    return x
