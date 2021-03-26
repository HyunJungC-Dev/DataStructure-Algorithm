import array


class BinaryTree:
    def __init__(self, arr):
        # 배열의 0번 index는
        # 계산의 편의성을 위해 사용하지 않는다.
        self.array = array.array('l', [-1]+arr)

    def preorder(self, idx):
        if idx > len(self.array)-1:
            return True
        print(self.array[idx])
        left_idx = idx*2
        right_idx = idx*2+1
        if left_idx <= len(self.array) - 1:
            self.preorder(left_idx)
        if right_idx <= len(self.array)-1:
            self.preorder(right_idx)

    def inorder(self):
        pass

    def postorder(self):
        pass

    def bfs(self, value):
        return False

    def dfs(self, value):
        return False


arr = [n for n in range(1,11)]
mybt = BinaryTree(arr)
print(mybt.array.tolist())
print("# Preorder")
mybt.preorder(1)
