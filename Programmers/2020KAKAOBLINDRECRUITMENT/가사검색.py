class Node:
    def __init__(self, data):
        self.data = data
        self.cnt = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        cur.cnt += 1

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.cnt += 1

    def count(self, prefix):
        cur = self.head

        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]

        return cur.cnt


def find_words(tries, reversed_tries, query):
    removed_whildcard_query = query.replace('?', '')

    if query[0] == '?':
        return reversed_tries[len(query)].count(removed_whildcard_query[::-1])
    else:
        return tries[len(query)].count(removed_whildcard_query)


def solution(words, queries):
    answer = []

    tries = {i: Trie() for i in range(1, 10001)}

    for word in words:
        tries[len(word)].insert(word)

    reversed_tries = {i: Trie() for i in range(1, 10001)}

    for word in words:
        word = word[::-1]
        reversed_tries[len(word)].insert(word)

    for query in queries:
        answer.append(find_words(tries, reversed_tries, query))

    return answer
