def solution(numbers):
    result = set()
    for idx, num in enumerate(numbers):
        numbers_len = len(numbers)
        idx += 1
        while(idx < numbers_len):
            result.add(num + numbers[idx])
            idx += 1
    result = list(result)
    result.sort()
    return result
