def binary_search(n, times):
    min_time = min(times[0])
    max_time = n*max(times[0])
    left = min_time
    right = max_time
    answer = 0

    while left <= right:
        mid = left + (right-left)//2
        expected_chicken_num = 0
        for i in range(len(times)):
            expected_chicken_num += mid//times[i][0]
            if mid % times[i][0] >= times[i][1]:
                expected_chicken_num += 1
            if expected_chicken_num >= n:
                right = mid-1
                answer = mid
                break

        if expected_chicken_num < n:
            left = mid+1

    return answer


n = int(input())
fry = list(map(int, input().split(' ')))
clean = list(map(int, input().split(' ')))
chickens = int(input())
times = []
for i in range(n):
    times.append((fry[i]+clean[i], fry[i]))

print(binary_search(chickens, times))
