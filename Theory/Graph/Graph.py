class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = set(adj_list)


class Graph:
    def __init__(self, vertex_num):
        self.vertex_num = vertex_num
        self.vertices = [Vertex(-1, None) for i in range(self.vertex_num)]

    def insert(self, value, adj_list):
        # value는 adj list 안 vertex 들과 연결한다.
        self.vertices[value] = Vertex(value, adj_list)
        for adj_vertex_idx in adj_list:
            self.vertices[adj_vertex_idx].adj_list.add(value)

    def bfs(self, vert_ind, value):
        visited = [-1 for i in range(self.vertex_num)]
        # visited = [False] * len(self.vertices)
        queue = []
        queue.append(vert_ind)
        while queue:
            curr_vertex_index = queue.pop(0)
            if visited[curr_vertex_index] != 1:
                visited[curr_vertex_index] = 1
                print(self.vertices[curr_vertex_index].value, end=' -> ')
                if self.vertices[curr_vertex_index].value == value:
                    return True
                for adj_idx in self.vertices[curr_vertex_index].adj_list:
                    if visited[adj_idx] != 1:
                        queue.append(adj_idx)
        return False

    def dfs(self, vert_ind, value):
        visited = [-1 for i in range(self.vertex_num)]
        stack = []
        stack.append(vert_ind)
        while stack:
            curr_vertex_idx = stack.pop()
            if visited[curr_vertex_idx] != 1:
                visited[curr_vertex_idx] = 1
                print(self.vertices[curr_vertex_idx].value, end=' -> ')
                if self.vertices[curr_vertex_idx].value == value:
                    return True
                for adj_idx in self.vertices[curr_vertex_idx].adj_list:
                    if visited[adj_idx] != 1:
                        stack.append(adj_idx)
        return False


myGraph = Graph(8)
myGraph.insert(0, [1, 2, 7])
myGraph.insert(1, [0, 3])
myGraph.insert(2, [0, 3, 6])
myGraph.insert(3, [1, 2, 4, 5])
myGraph.insert(4, [3, 5])
myGraph.insert(5, [3, 4, 6, 7])
myGraph.insert(6, [2, 5, 7])
myGraph.insert(7, [0, 5, 6])


#print([(i.value, i.adj_list) for i in myGraph.vertices])

print(myGraph.bfs(0, 7))
print(myGraph.dfs(0, 1))
