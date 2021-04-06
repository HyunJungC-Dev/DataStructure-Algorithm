# 백준 2748번 - 피보나치 수 2

import collections

n = int(input())


def solution(n):
    dp = collections.defaultdict(int)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


print(solution(n))
