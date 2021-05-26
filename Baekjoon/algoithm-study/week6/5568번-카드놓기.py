import itertools

n = int(input())
k = int(input())
nums = []
for _ in range(n):
    nums.append(input())

all_make = list(itertools.permutations(nums, k))

removed_overlap = set()
for cards in all_make:
    tmp = ""
    for card in cards:
        tmp += card
    removed_overlap.add(tmp)
print(len(removed_overlap))
