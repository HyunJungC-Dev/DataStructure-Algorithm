class Node:
    # 탐색한 노드인지 확인하기 위한 visited 추가
    def __init__(self, value, left, right, visited):
        self.value = value
        self.left = left
        self.right = right
        self.visited = False


class BinaryTree:
    def __init__(self, array):
        # 위에서 visited를 추가했으니 ,None을 추가
        node_list = [Node(value, None, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    # node -> left-> right
    def preorder(self):
        stack = []
        if self.root is None:
            return None
        else:
            stack.append(self.root)
            while stack:
                curr_node = stack.pop()
                print(curr_node.value, end=' ')
                if curr_node.right is not None:
                    stack.append(curr_node.right)
                if curr_node.left is not None:
                    stack.append(curr_node.left)

    # left->node->right
    def inorder(self):
        pass

    def postorder(self):
        pass

    def bfs(self, value):
        return False

    def dfs(self, value):
        return False


arr = [n for n in range(1, 11)]
myBT = BinaryTree(arr)
myBT.preorder()
