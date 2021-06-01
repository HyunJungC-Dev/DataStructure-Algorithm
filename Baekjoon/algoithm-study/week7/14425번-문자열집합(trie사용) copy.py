import collections
import sys
n, m = map(int, sys.stdin.readline().strip().split(' '))


class Node:
    def __init__(self, data):
        self.data = data
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head

        for c in string:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
        curr.child['*'] = Node('*')

    def isIn(self, target):
        curr = self.head
        target += '*'
        for c in target:
            if c not in curr.child:
                return False
            curr = curr.child[c]

        return True


tries = Trie()
for _ in range(n):
    tries.insert(sys.stdin.readline().strip())

cntInSet = 0
for _ in range(m):
    if tries.isIn(sys.stdin.readline().strip()):
        cntInSet += 1

print(cntInSet)
