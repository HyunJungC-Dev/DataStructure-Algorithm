import heapq

n = int(input())
edges = [[(2, 4), (3, 1)],
         [(4, 2), (0, 4)],
         [(1, 4)],
         [(4, 1)],
         [(3, 7)]]


def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n
    heapq.heappush(heap, (0, start))
    while heap:
        d, v = heapq.heappop(heap)
        if distances[v] < d:
            continue
        distances[v] = d
        for ad_v in graph[v]:
            if distances[v] + ad_v[1] < distances[ad_v[0]]:
                distances[ad_v[0]] = distances[v]+ad_v[1]
                heapq.heappush(heap, (distances[ad_v[0]], ad_v[0]))
    return distances


distances = dijkstra(0, edges)
is_connected = True
answer = 0
for i in range(n):
    if distances[i] == float('inf'):
        is_connected = False
        print(-1)
        break
    else:
        answer = max(answer, distances[i])
if is_connected:
    print(answer)
