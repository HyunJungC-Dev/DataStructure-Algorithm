class Node:
    def __init__(self, vertex_num):
        self.vertex_num = vertex_num
        self.parent_node = self


def find_root(vertex_node: Node):
    curr = vertex_node
    while curr.vertex_num != curr.parent_node.vertex_num:
        curr = curr.parent_node
    return curr.vertex_num


def union(vertex_node1: Node, vertex_node2: Node):
    vn1_root = find_root(vertex_node1)
    vn2_root = find_root(vertex_node2)

    if vn1_root != vn2_root:
        vertex_node2.parent_node = vertex_node1
        return True
    return False


def kruskal(graph):
    # edge로 추출
    edges = []
    vetexs = [Node(i) for i in range(len(graph))]
    for vertex_idx, adj_list in enumerate(graph):
        for ad_v in adj_list:
            if ad_v[0] > vertex_idx:
                edges.append((ad_v[1], vetexs[vertex_idx], vetexs[ad_v[0]]))
    edges = sorted(edges)

    mst = []
    for e in edges:
        if union(e[1], e[2]):
            mst.append((e[0], e[1].vertex_num, e[2].vertex_num))
            if len(mst) == len(graph)-1:
                return mst


graph = [[(1, 28), (5, 10)],  # (인접노드, 가중치)
         [(0, 28), (2, 16), (6, 14)],
         [(1, 16), (3, 12)],
         [(2, 12), (4, 22), (6, 18)],
         [(3, 22), (5, 25), (6, 24)],
         [(0, 10), (4, 25)],
         [(1, 14), (3, 18), (4, 24)]]
print(kruskal(graph))
