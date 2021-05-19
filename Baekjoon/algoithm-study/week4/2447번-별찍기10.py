n = int(input())

star = [["*" for _ in range(n)] for _ in range(n)]


def recursive(s_i, s_j, k):  # start i, start j
    if k == 0:
        return
    for i in range(s_i+(k//3), s_i+((k//3)*2)):
        for j in range(s_j+(k//3), s_j+((k//3)*2)):
            star[i][j] = ' '

    recursive(s_i, s_j, k//3)
    recursive(s_i, s_j+(k//3), k//3)
    recursive(s_i, s_j+((k//3)*2), k//3)
    recursive(s_i+(k//3), s_j, k//3)
    recursive(s_i+((k//3)*2), s_j, k//3)
    # recursive(s_i+(k//3), s_j+(k//3), k//3)
    recursive(s_i+((k//3)*2), s_j+(k//3), k//3)
    recursive(s_i+(k//3), s_j+((k//3)*2), k//3)
    recursive(s_i+((k//3)*2), s_j+((k//3)*2), k//3)


recursive(0, 0, n)

# tmp = n
# k = 0
# while tmp != 1:
#     tmp //= 3
#     k += 1
# for curr_k in range(k):
#     blank_loc = [idx for idx in range(n) if(idx//3**curr_k) % 3 == 1]
#     for i in blank_loc:
#         for j in blank_loc:
#             star[i][j] = " "
for i in range(n):
    for j in range(n):
        print(star[i][j], end='')
    print()
