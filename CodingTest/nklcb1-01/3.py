import array
n = int(input())

amoeba = [None] * (2**(n))
print(amoeba)
time = 1
amoeba[1] = True
for _ in range(n):
    for idx in range(2**(time-1)):
        if amoeba[idx] is False:
            amoeba[idx] = True
            left_idx = idx*2
            right_idx = idx*2+1
            if left_idx < 2**n:
                amoeba[left_idx] = True
            if right_idx < 2**n:
                amoeba[right_idx] = False
    for idx in range(2**(time-1), 2**time):
        if amoeba[idx] is True:
            left_idx = idx*2
            right_idx = idx*2+1
            if left_idx < 2**n:
                amoeba[left_idx] = True
            if right_idx < 2**n:
                amoeba[right_idx] = False
    time += 1

answer = 0
for idx in range(2**n):
    left_idx = idx*2
    right_idx = idx*2+1
    if amoeba[idx] is None:
        pass
    elif amoeba[idx] is True:
        answer += 1
print(answer)
