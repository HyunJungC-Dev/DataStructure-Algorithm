import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.cnt = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head
        curr.cnt += 1

        for c in string:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
            curr.cnt += 1

    def count(self, prefix):
        curr = self.head

        for c in prefix:
            if c not in curr.child:
                return 0
            curr = curr.child[c]

        return curr.cnt


def find_words(tries, reversed_tries, query):
    removed_whildcard_query = query.replace('?', '')

    if query[0] == '?':
        return reversed_tries[len(query)].count(removed_whildcard_query[::-1])
    else:
        return tries[len(query)].count(removed_whildcard_query)


def solution(words, queries):
    answer = []

    tries = collections.defaultdict(Trie)  # 검색 키워드의 길이는 1 이상 10,000 이하

    for word in words:
        tries[len(word)].insert(word)

    reversed_tries = collections.defaultdict(Trie)

    for word in words:
        word = word[::-1]
        reversed_tries[len(word)].insert(word)

    for query in queries:
        answer.append(find_words(tries, reversed_tries, query))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
