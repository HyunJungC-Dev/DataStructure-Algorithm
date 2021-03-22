def solution(numbers):
    result = set() # 두 수의 덧셈으로 가능한 경우를 저장 - set을 이용해 겹치는 경우 제외
    # 각 원소들이 자신보다 뒤 인덱스에 있는 모든 원소와 덧셈하여 set인 result에 추가
    for idx, num in enumerate(numbers):
        numbers_len = len(numbers)
        idx += 1
        while(idx < numbers_len):
            result.add(num + numbers[idx])
            idx += 1
    result = list(result) # set을 list로 변경
    result.sort() # list를 오름차순으로 정렬
    return result
