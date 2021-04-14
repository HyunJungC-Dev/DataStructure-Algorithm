import heapq

# Min Heap
heap = []  # 힙으로 사용할 리스트 생성
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

print(heapq.heappop(heap))  # 1 힙에서 최소값 추출 (Min heap으로 동작)
print(heapq.heappop(heap))  # 2
print(heapq.heappop(heap))  # 5


# Max Heap
# Max Heap으로 사용하고자 할 경우, 자료를 입력할 때 튜플로 우선순위를 추가한다.
# (우선순위, value)로 구현
heap = []  # 힙으로 사용할 리스트 생성
heapq.heappush(heap, (-2, 2))  # 힙에 자료 입력 (-val, val)으로 우선순위를 추가
heapq.heappush(heap, (-1, 1))
heapq.heappush(heap, (-5, 5))

print(heapq.heappop(heap)[1])  # 5 힙에서 최소값 추출 (Max heap으로 동작)
print(heapq.heappop(heap)[1])  # 2
print(heapq.heappop(heap)[1])  # 1

heap = [1, 2, 3, 4, 5, 6, 7]
heapq.heapify(heap)
print(heap)
heap = [7,6,5,4,3,2,1]
heapq.heapify(heap)
print(heap)

