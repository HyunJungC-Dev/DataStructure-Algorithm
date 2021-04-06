# 백준 9095번 - 1,2,3 더하기
import collections

T = int(input())

while T:
    n = int(input())
    dp = collections.defaultdict(int)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
    T -= 1
