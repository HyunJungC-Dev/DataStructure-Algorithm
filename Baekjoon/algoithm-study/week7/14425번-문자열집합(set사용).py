import sys
n, m = map(int, sys.stdin.readline().strip().split(' '))

strings = set()
for _ in range(n):
    strings.add(sys.stdin.readline().strip())

cntInSet = 0
for _ in range(m):
    if sys.stdin.readline().strip() in strings:
        cntInSet += 1

print(cntInSet)