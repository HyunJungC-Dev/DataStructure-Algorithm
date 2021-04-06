# 점화식 dp[n] = dp[n-1] + dp[n-2]
n = int(input())


def solution(n):
    x = 1
    y = 2
    for _ in range(n-2):
        x, y = y, x+y
    return y % 10007


print(solution(n))
