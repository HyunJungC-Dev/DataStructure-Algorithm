import array


class BinaryTree:
    def __init__(self, arr):
        # 배열의 0번 index는
        # 계산의 편의성을 위해 사용하지 않는다.
        self.array = array.array('l', [-1]+arr)

    # node->left->right
    def preorder(self, idx):
        print(self.array[idx])
        left_idx = idx*2
        right_idx = idx*2+1
        if left_idx <= len(self.array) - 1:
            self.preorder(left_idx)
        if right_idx <= len(self.array)-1:
            self.preorder(right_idx)

    # left->node->right
    def inorder(self, idx):
        left_idx = idx*2
        right_idx = idx*2+1
        if left_idx <= len(self.array)-1:
            self.inorder(left_idx)
        print(self.array[idx])
        if right_idx <= len(self.array)-1:
            self.inorder(right_idx)

    # left->right->node
    def postorder(self, idx):
        left_idx = idx*2
        right_idx = idx*2+1
        if left_idx <= len(self.array)-1:
            self.postorder(left_idx)
        if right_idx <= len(self.array)-1:
            self.postorder(right_idx)
        print(self.array[idx])

    # 해당 value의 존재 여부 확인
    def bfs(self, value):
        for i in range(1, len(self.array)-1):
            if self.array[i] == value:
                return True
        return False

    def dfs(self, value, idx):
        if value == self.array[idx]:
            return True
        left_idx = idx*2
        right_idx = idx*2+1
        if left_idx <= len(self.array) - 1:
            if self.dfs(value, left_idx) is True:
                return True

        if right_idx <= len(self.array)-1:
            if self.dfs(value, right_idx) is True:
                return True


arr = [n for n in range(1, 11)]
mybt = BinaryTree(arr)
print(mybt.array.tolist())
print("# Preorder")
mybt.preorder(1)
print("# Inorder")
mybt.inorder(1)
print("# Postorder")
mybt.postorder(1)
print("# BFS")
print("is {value} in Tree? : {result}".format(value=3, result=mybt.bfs(13)))
print("# DFS")
print("is {value} in Tree? : {result}".format(value=3, result=mybt.dfs(11, 1)))
