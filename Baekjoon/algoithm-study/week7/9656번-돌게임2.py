import sys
n = int(sys.stdin.readline().strip())
remainder = n % 4

if remainder == 0 or remainder == 2:
    print("SK")
else:
    print("CY")

"""
상근이 + 창영이 무조건 짝수
1 1 -> 2
1 3 -> 4
3 1 -> 4

4로 나눈 나머지가 0이면 상근이가 무조건 이김
4로 나눈 나머지가 1이면 무조건 창영이가 이김
창영이가 계속 4가 되도록 가져갈 것이기 때문
4로 나눈 나머지가 2이면 상근이가 무조건 이김
4로 나눈 나머지가 3이면 창영이가 무조건 이김

정확히는 짝수면 상근이가, 홀수면 창영이가 이긴다.
"""
