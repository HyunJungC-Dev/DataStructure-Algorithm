import heapq


def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n
    path = [[]for i in range(len(graph))]
    path[start].append(start)

    heapq.heappush(heap, (0, start))
    distances[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distances[node]:
            continue

        for adj_node, adj_dist in graph[node]:
            new_dist = dist + adj_dist
            if new_dist < distances[adj_node]:
                distances[adj_node] = new_dist
                heapq.heappush(heap, (new_dist, adj_node))
                path[adj_node] = [adj_node] + path[node]
    print(path)
    return distances


graph = [[(1, 2), (2, 5)],
         [],
         [(1, -10)]]

print(dijkstra(0, graph))
