from ..list_implementation import DoublyLinkedList

"""
DoublyLinkedList의 추상화된 메소드만 가지고도
그 안의 내용을 건드리지 않고도, Queue를 구현할 수 있다.
"""


class ComposedLinkedQueue:  # 1. Composited
    def __init__(self):
        self.dll = DoublyLinkedList()  # Coposition

    def put(self, value):
        return self.dll.append(value)

    def get(self):
        value = self.dll.access(0)
        if value is not None:
            self.dll.remove(0)
        return value

    def peek(self):
        return self.dll.access(0)

    def print(self):
        self.dll.print()


class DerivedLinkedQueue(DoublyLinkedList):  # 상속에 의한 구현 (Inheritance)
    def __init__(self):
        super().__init__()

    def put(self, value):
        # super().append(value)
        # self.append(value) 가 맞음. super()는 오버라이딩 되어있지 않아서 부모쪽 메소드를 가져와 쓴다는 의미가 된다.
        self.append(value)  # self가 들어간다는 것 = 다형성의 의미를 가진다.

    def get(self):
        value = self.access(0)
        if value is not None:
            self.remove(0)
        return value

    def peek(self):
        return self.access(0)

    def print(self):
        super().print()  # super()를 이용해서 부모객체에 접근해야한다.
        # self.print()해주면 자기 자신을 재귀호출해서 무한 루프에 걸려 파이썬이 죽는다.
        # 파이썬은 998번의 recurcion이 가능하다. 그걸 지나면 죽어버린다.
