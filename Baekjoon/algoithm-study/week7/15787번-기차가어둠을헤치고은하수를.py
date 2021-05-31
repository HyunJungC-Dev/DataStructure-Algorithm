import sys

n, m = map(int, sys.stdin.readline().split(' '))
train = [0 for _ in range(n+1)]  # 요소 0000 0000 0000 0000 0000
for _ in range(m):
    tmpCmd = sys.stdin.readline().strip().split(' ')
    num = int(tmpCmd[0])
    i = int(tmpCmd[1])

    if num == 1:
        x = int(tmpCmd[2])
        train[i] |= (1 << x)  # 0이든 1이든 1로
    elif num == 2:
        x = int(tmpCmd[2])
        train[i] &= ~(1 << x)  # 0이든 1이든 0으로
    elif num == 3:
        train[i] = (train[i] << 1)
        train[i] &= ~(1 << 21)
    elif num == 4:
        train[i] = (train[i] >> 1)
        train[i] &= ~1

canCrossing = set()
for i in range(1, n+1):
    canCrossing.add(train[i])
print(len(canCrossing))
