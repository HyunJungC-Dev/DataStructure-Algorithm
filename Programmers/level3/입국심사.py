def solution(n, times):
    min_time = min(times)
    max_time = n*max(times)
    left = min_time
    right = max_time
    answer = 0

    while left <= right:
        mid = left + (right-left)//2
        expected_people_num = 0
        for time in times:
            expected_people_num += mid//time
            if expected_people_num >= n:
                right = mid-1
                answer = mid
                break

        if expected_people_num < n:
            left = mid+1

    return answer
