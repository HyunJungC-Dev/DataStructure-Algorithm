# n : 물품의 수, k : 버틸 수 있는 무게
n, k = map(lambda x: int(x), input().split())

cargo = [(-1, -1)]
cnt = n
while cnt:
    w, v = map(lambda x: int(x), input().split())
    cargo.append((w, v))
    cnt -= 1

dp = [[0 for col in range(k+1)] for row in range(2)]

for c_idx in range(1, n+1):
    for curr_k in range(1, k+1):
        if cargo[c_idx][0] > curr_k:
            dp[c_idx % 2][curr_k] = dp[(c_idx-1) % 2][curr_k]
        else:
            dp[c_idx % 2][curr_k] = max(
                dp[(c_idx-1) % 2][curr_k],
                dp[(c_idx-1) % 2][curr_k-cargo[c_idx][0]] + cargo[c_idx][1])
print(dp[n % 2][k])
