# 백준 1463번 - 1로 만들기
import collections

n = int(input())


def solution(n):
    dp = collections.defaultdict(int)
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = dp[i-1]+1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i/3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i/2] + 1)

    return dp[n]


print(solution(n))
