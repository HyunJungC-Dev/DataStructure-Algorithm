class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = adj_list


class Graph:
    def __init__(self):
        self.vertices = []

    def insert(self, value, adj_list):
        self.vertices.append(Vertex(value, adj_list))
        for adj_ind in adj_list:
            self.vertices[adj_ind].adj_list.append(len(self.vertices) - 1)

    def bfs(self, vert_ind, value):
        queue = []
        queue.append(vert_ind)
        visited = [False]*len(self.vertices)

        while queue:
            v_idx = queue.pop(0)
            v = self.vertices[v_idx]

            if visited[v_idx]:
                continue

            visited[v_idx] = True

            print(self.vertices[v_idx].value, end=' -> ')

            if v.value == value:
                return True

            for adj_v_idx in v.adj_list:
                if visited[adj_v_idx] is False:
                    queue.append(adj_v_idx)
        return False

    def dfs(self, vert_ind, value):
        isFound = False
        visited = [False] * len(self.vertices)

        def recursive(idx):
            nonlocal isFound
            # visited는 단순히 객체에 접근하는 것뿐이라 nonlocal을 해주지 않아도 된다.

            # 밑에서 검사하므로 queue와 달리 생략해도 된다.
            # if isFound:
            #     return

            visited[idx] = True
            v = self.vertices[idx]
            print(v.value, end=' -> ')
            if v.value == value:
                isFound = True
                return
            for adj_v_idx in v.adj_list:
                if visited[adj_v_idx] is False:
                    recursive(adj_v_idx)
        recursive(vert_ind)
        return isFound


graph = Graph()
graph.insert(0, [])
graph.insert(1, [0])
graph.insert(2, [0])
graph.insert(3, [1, 2])
graph.insert(4, [3])
graph.insert(5, [3, 4])
graph.insert(6, [2, 5])
graph.insert(7, [0, 5, 6])

print(graph.bfs(0, 7))
print(graph.dfs(0, 1))
