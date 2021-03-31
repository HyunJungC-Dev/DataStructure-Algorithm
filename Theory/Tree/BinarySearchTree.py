import random


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __serch(self, value):
        node = self.root
        parent = None
        direction = None

        while node:
            if node.value == value:
                break
            elif value < node.value:
                parent = node
                node = node.left
                direction = 'left'
            else:
                parent = node
                node = node.right
                direction = 'right'
        return node, parent, direction

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None, None)
            return True
        else:
            curr_node = self.root
            while curr_node:
                if value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = Node(value, None, None)
                        return True
                    else:
                        curr_node = curr_node.left
                elif value > curr_node.value:
                    if curr_node.right is None:
                        curr_node.right = Node(value, None, None)
                        return True
                    else:
                        curr_node = curr_node.right
                elif value == curr_node.value:
                    return False

    def search(self, value):
        if self.root is None:
            return False
        else:
            curr_node = self.root
            while curr_node:
                if curr_node.value == value:
                    return True
                elif curr_node.value < curr_node.left:
                    curr_node = curr_node.left
                elif curr_node.value > curr_node.right:
                    curr_node = curr_node.right

    def __findMin(self, start_node):
        node = start_node
        parent = None

        while node.left:
            parent = node
            node = node.left
        return node, parent

    def __connect(self, child, parent, direction):
        if direction == 'left':
            parent.left = child
        else:
            parent.right = child

    def remove(self, value):
        pass


mybst = BinarySearchTree()

x = list(range(1, 20))
random.shuffle(x)
print(x)
for el in x:
    mybst.insert(el)
mybst.root.display()
# print(mybst._BinarySearchTree__findMin(mybst.root)[0].value)
random.shuffle(x)
# for el in x:
#     print(el)
#     mybst.remove(el)
#     mybst.root.display()
mybst.remove(5)
mybst.root.display()

# mybst.remove(10)
# mybst.root.display()
