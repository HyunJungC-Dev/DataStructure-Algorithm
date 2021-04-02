def solution(n):
    def hanoi(n, a, b, c):
        if n == 1:
            return [[a, c]]
        return hanoi(n-1, a, c, b) + [[a, c]] + hanoi(n-1, b, a, c)

    return hanoi(n, 1, 2, 3)