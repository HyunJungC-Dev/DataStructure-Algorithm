def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left = 0
    right = distance
    while left <= right:
        mid = left + (right-left)//2
        removed_rocks_cnt = 0
        curr = 0
        for rock in rocks:
            between_distance = rock - curr
            if between_distance < mid:
                removed_rocks_cnt += 1
            else:
                curr = rock
        if removed_rocks_cnt <= n:
            answer = mid  # answer보다 mid가 항상 크다.
            left = mid+1
        else:
            right = mid-1

    return answer
