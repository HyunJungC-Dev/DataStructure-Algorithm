def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left = 0
    right = distance
    answer = 0
    while left <= right:
        mid = left + (right-left)//2
        removed_rocks_cnt = 0
        curr = 0
        min_distance = float('inf')
        for rock in rocks:
            # mid 보다 작으면 다 지운다. = 그래야 mid가 최소값이 된다.
            between_distance = rock - curr
            if between_distance >= mid:
                curr = rock
                min_distance = min(min_distance, between_distance)
            elif between_distance < mid:
                removed_rocks_cnt += 1
                if removed_rocks_cnt > n:
                    right = mid - 1
                    break
        if removed_rocks_cnt <= n:
            left = mid+1
            answer = min_distance

    return answer
