n = int(input())
d = int(input())
x = list(map(int, input().split(' ')))
len_street = len(x)
dp = [0]*len_street
cnt_rabbit = 0
for i in range(len_street):
    if x[i] == 1:
        cnt_rabbit += 1
    dp[i] = cnt_rabbit

s, e = 0, 1

curr_net = 0
min_net = float('inf')
while s < e and e < len_street:
    if s == 0:
        if dp[e] >= n:
            min_net = min(curr_net, min_net)
            s += 1
        else:
            e += 1
            curr_net += 1

    elif dp[e]-dp[s-1] >= n:
        min_net = min(curr_net, min_net)
        s += 1
    else:
        e += 1
        curr_net += 1


if min_net == float('inf'):
    print(-1)
else:
    print(min_net)
