class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):  # enumerate 는 tuple로 붂여서 나온다.
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    # node -> left-> right
    def preorder(self):
        pass
    # left->node->right

    def inorder(self):
        pass
    # left-> right -> node

    def postorder(self):
        pass

    def bfs(self, value):
        queue = []
        if self.root is None:
            return False
        else:
            queue.append(self.root)  # put
            while queue:
                node = queue.pop(0)  # get

                """
                Truthy, Falsy
                Truthy : True, 차있는 list, 0이 아닌 숫자(음수 포함), None이 아닌 참조
                Falsy : False, 비어있는 list, 숫자 0, None인 참조

                == , is
                == 는 값을 비교해서 같으면 True
                is 는 동일한 객체인지를 확인해서 같으면 True (id()를 비교하여 확인, 이 id가 reference이다.)
                
                파이썬에서는 id()가 유일하게 객체를 구분하는 수단(주소값은 알 수 없다.)
                이 id()가 즉, 참조이다.
                -> 파이썬은 전부 call by referce이다.
                """

                if node.value == value:
                    return True

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

    def dfs_recursive(self, value):
        isFound = False

        def recursive(node):
            nonlocal isFound

            if node is None:
                return

            if isFound:
                return

            if node.value == value:
                isFound = True
                return True

            if node.left:
                recursive(node.left)

            if node.right:
                recursive(node.right)
        recursive(self..root)

    def dfs(self, value):
        stack = []
        if self.root is None:
            return False
        else:
            stack.append(self.root)  # push
            while stack:
                curr_node = stack.pop()  # pop

                if curr_node.value == value:
                    return True

                if curr_node.right:
                    stack.append(curr_node.right)

                if curr_node.left:
                    stack.append(curr_node.left)
            return False


"""
recursive 보다 stack이 훨씬 좋다.
대신 이거는 해석이 더 어렵다.
998번 recursive() 제한도 없고 메모리도 덜 쓴다.
"""

arr = [n for n in range(1, 11)]
myBT = BinaryTree(arr)
myBT.preorder()
myBT.inorder()
myBT.postorder()
v = 2
if myBT.bfs(v) is True:
    print(v, "is in this Binary Tree")
else:
    print(v, "is not in this Binary Tree")
if myBT.dfs(v) is True:
    print(v, "is in this Binary Tree")
else:
    print(v, "is not in this Binary Tree")
