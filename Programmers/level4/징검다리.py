def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        min_distance = -1
        current = 0
        remove_cnt = 0

        for rock in rocks:
            between_dis = rock - current
            if between_dis < mid:
                remove_cnt += 1
            else:
                current = rock
                min_distance = min(min_distance, between_dis)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer
