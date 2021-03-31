def solution(x, y):
    return x+y


def outer(n):
    def inner(x):
        return x + n
    return inner


def outer():
    outer_sum = 0

    def inner(x):
        nonlocal outer_sum  # 외부 값을 수정하가 위해 필요
        outer_sum += x
        return outer_sum
    return inner


"""
List Comprehension 기본 문법
[(변수를 활용한 값 = 계산) for (사용할 변수 이름) in (순회할 수 있는 값)]
"""
arr_size = 10
arr = [x for x in range(arr_size)]
print(arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = [x*2 for x in range(arr_size)]
print(arr)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

arr2 = [n*n for n in arr]
print(arr2)  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

word = "가나다라마"
arr3 = [c*2 for c in word]
print(arr3)  # ['가가', '나나', '다다', '라라', '마마']
"""
if문 + list comprehesion
if문 사이에 and 쓰면 SyntaxError
2의 배수 이고 3의 배수
"""
arr = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]
print(arr)  # [6, 12, 18, 24, 30]

"""
if 문 사이에 or 쓰면 SyntaxError
if문 두 개를 or 하면 SyntaxError 발생
2의 배수 하나의 if 안에 or 3의 배수
"""
arr = [n for n in range(1, 31) if n % 2 == 0 or n % 3 == 0]
print(arr)

"""
차원 축소
리스트 안에 리스트가 있는 다차원 리스트의 차원을 하나 축소할 수 있다.

아래의 경우 2차원 배열 -> 1차원 배열로 축소
flat_one = [n for row in arr for n in row]
행을 다루는 for문 다음 행 안의 셀을 다루는 for문
"""
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12]
       ]

flat_one = [n for row in arr for n in row]
print(flat_one)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""
위와 같은 list comprehension
"""
flat_one2 = []
for row in arr:
    for n in row:
        flat_one2.append(n)
print(flat_one2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""
3차원 배열 -> 2차원 배열 -> 1차원 배열
"""
arr = [
    [[1, 2], [3, 4], [5, 6]],
    [[7, 8], [9, 10], [11, 12]],
    [[13, 14], [15, 16], [17, 18]],
    [[19, 20], [21, 22], [23, 24]]
]

flat_two = [n for row in arr for n in row]
# [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24]]
print(flat_two)

flat_one3 = [n for row in flat_two for n in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print(flat_one3)


"""
2차원을 유지하면서 내부 리스트 연산
"""
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12]
       ]

squared_list = [[n**2 for n in row] for row in arr]
print(squared_list)  # [[1, 4, 9], [16, 25, 36], [49, 64, 81], [100, 121, 144]]
"""
[n**2 for n in row] 를 A로 치환하면
squared_list = [A for row in arr]
"""
