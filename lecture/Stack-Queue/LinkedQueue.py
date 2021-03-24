class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        # 맨 뒤 노드 삽입
        # 비어 있다면 지금 넣는 게 첫 노드인 것
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            # 원래 taill 뒤에 put한 node를 붙이고
            # put한 node를 tail뒤에 붙이고
            self.tail.next = Node(value, self.tail, None)
            # tail을 put 한 걸로 바꾸고
            self.tail = self.tail.next

    def get(self):
        # 맨 앞 노드 삭제
        # 만약 비어 있다면
        if self.head is None:
            print("Underflow")
            return None
        # 아무튼 하나라도 뺄 게 있다면
        value = self.head.value
        # !!!노드가 하나만 존재한다면!!!
        if self.head.next is None:
            # 삭제하고 나면 empty가 됨.
            self.tail = None
            self.head = None
            return value

        # 맨 앞 노드 다음이 head가 된다.
        self.head = self.head.next
        # head의 prev는 None이 되어야한다.
        self.head.prev = None
        return value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def print(self):
        print('<- ', end='')
        curr = self.head
        while curr is not None:
            print(curr.value, end=' ')
            curr = curr.next
        print('<-')


print("------------------------")
myLinkedQueue = LinkedQueue()
print("1. LinkedQueue에 1 삽입")
myLinkedQueue.put(1)
myLinkedQueue.print()
print("2. LinkedQueue에 2 삽입")
myLinkedQueue.put(2)
myLinkedQueue.print()
print("3. LinkedQueue에 3 삽입")
myLinkedQueue.put(3)
myLinkedQueue.print()
print("4. LinkedQueue에서 get")
print("get : ", myLinkedQueue.get())
myLinkedQueue.print()
print("5. LinkedQueue에서 get")
print("get : ", myLinkedQueue.get())
myLinkedQueue.print()
print("6. LinkedQueue에서 get")
print("get : ", myLinkedQueue.get())
myLinkedQueue.print()
print("7. 비어있는 LinkedQueue에서 get - Underflow")
print("get : ", myLinkedQueue.get())
myLinkedQueue.print()
print("8. LinkedQueue에 5 put")
myLinkedQueue.put(5)
myLinkedQueue.print()
print("9. LinkedQueue에 6 put")
myLinkedQueue.put(6)
myLinkedQueue.print()
print("10. LinkedQueue에 7 put")
myLinkedQueue.put(7)
myLinkedQueue.print()
print("11. LinkedQueue에서 peek")
print("peek : ", myLinkedQueue.peek())
myLinkedQueue.print()
