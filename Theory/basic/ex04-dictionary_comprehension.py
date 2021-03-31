"""
Dictionary Comprehension

"""
from string import ascii_lowercase as LOWERS
a = {key: key**2 for key in range(10)}

print(a)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

"""
zip 함수
zip(*iterable) 은 
동일한 개수로 이루어진 자료형을
묶어 주는 함수이다. 
"""
print(list(zip([1, 2, 3], [4, 5, 6])))
# [(1, 4), (2, 5), (3, 6)]

print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

print(list(zip("abc", "def")))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]


dict_alp = {c: n for c, n in zip(LOWERS, range(1, 27))}
print(dict_alp)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
# 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
# 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
