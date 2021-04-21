n = int(input())

nums = list(map(int, input().split(' ')))
# print(nums)

# dp[i]는 i번째 원소를 마지막으로하는 수열 중 가장 긴 증가하는 부분수열
dp = [1]*n
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)
# print(dp)
print(max(dp))
