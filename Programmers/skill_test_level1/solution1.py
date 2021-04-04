def solution(s):
    cnt_p = 0 # p와 P의 개수를 저장 
    cnt_y = 0 # y와 Y의 개수를 저장
    for i in s:
        if i == 'p' or i == 'P':
            cnt_p += 1
        elif i == 'y' or i == 'Y':
            cnt_y += 1

    return cnt_p == cnt_y
