# input x : list
def bubble_sort(x):
    length = len(x)-1  # 자기 다음과 비교하므로 마지막 요소는 확인할 필요 없음
    for i in range(length):  # 이 for 문을 한번 돌면 가장 큰 게 맨 뒤로 가 있다.
        swapped = False
        for j in range(length-i):  # 자기 앞은 보지 않음.
            if x[j] > x[j+1]:  # 앞이 뒤보다 크면
                swapped = True
                x[j], x[j+1] = x[j+1], x[j]  # swap
        if swapped is False:  # 더이상 swap이 없음 = 정렬이 끝남.
            break
    return x
