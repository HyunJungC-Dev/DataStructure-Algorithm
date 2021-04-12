import heapq


def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n
    # 시작노드를 heap에 (자기자신까리 거리 0, 시작 노드) 를 push
    heapq.heappush(heap, (0, start))
    # heap이 빌 때까지
    while heap:
        d, v = heapq.heappop(heap)  # heap에서 pop
        if distances[v] < d:  # 만약 pop한 노드의 거리가 distance[]에 저장된 거리보다 길다면
            continue  # 스킵한다.
        distances[v] = d
        for ad_v in graph[v]:
            if distances[v] + ad_v[1] < distances[ad_v[0]]:
                distances[ad_v[0]] = distances[v]+ad_v[1]
                heapq.heappush(heap, (distances[ad_v[0]], ad_v[0]))
    


graph = [[(2, 5), (3, 2)],  # (인접노드, 가중치)
         [(3, 5), (4, 3)],
         [(0, 3), (4, 9)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]

dijkstra(0, graph)
dijkstra(1, graph)
dijkstra(2, graph)
