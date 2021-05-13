
n = int(input())
start = input()
end = input()
counts = input().split(' ')

# a: 97 z: 122 A: 65 Z: 90


def nToten(str_n):
    base_ten = 0
    mul = 1
    for i in range(len(str_n)-1, -1, -1):
        tmp_n = alpTonum(str_n[i])
        base_ten += tmp_n * mul
        mul *= n
    return base_ten


def alpTonum(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return ord(c)-87
    elif ord(c) >= 65 and ord(c) <= 90:
        return ord(c)-29
    else:
        return int(c)


correct_counts = [i for i in range(nToten(start), nToten(end)+1)]

curr = nToten(start)
for _ in range(len(counts)):
    correct_counts.append(curr)
    curr += 1
    if curr+1 >= n:
        curr = 0
error_cnt = 0
for i in range(len(counts)):
    if nToten(counts[i]) != correct_counts[i]:
        error_cnt += 1
print(error_cnt)
