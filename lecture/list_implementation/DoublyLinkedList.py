class Node:
    # prev 와 next의 순서를 변경하였습니다.
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    # 더블 링크드 리스트 생성
    def __init__(self):
        self.head = None
        self.tail = None

    # 더블 링크드 리스트가 비어있는 지 확인
    def is_empty(self):
        # head 가 None 이면 링크드리스트에 아무것도 없는 것이다.
        return self.head is None

   # 더블 링크드 리스트의 맨 앞에 요소 추가
    def prepend(self, value):
        # 더블 링크드 리스트가 비어있다면
        if self.is_empty():
            # 앞을 가리키는 prev와
            # 뒤를 가리키는 next엔 None이 들어간다.
            self.head = Node(value, None, None)
            # 요소가 하나뿐이므로
            # head와 tail이 모두 같은 노드를 가리킨다.
            self.tail = self.head
        # 더블 링크드 리스트에 다른 요소가 있다면
        else:
            # 원래 head가
            before_head = self.head
            # 새로 맨 앞에 추가한 노드의 next가 되고
            # 새로 추가한 노드의 주소가 새 head가 된다.
            # 새로 추가한 노드의 prev엔
            # 새로 추가한 노드가 맨 앞이므로 None을 넣는다.
            self.head = Node(value, None, before_head)
            # 맨 앞에 추가했으므로 self.tail 은 바뀌지 않는다.

    # 더블 링크드 리스트 맨 뒤에 요소 추가
    def append(self, value):
        # 더블 링크드 리스트가 비어있다면
        if self.is_empty():
            # prepend와 동일하다.
            self.head = Node(value, None, None)
            self.tail = self.head
        # 더블 링크드 리스트에 다른 요소가 있다면
        else:
            # 원래 tail이
            before_tail = self.tail
            # 새로 맨 뒤에 추가한 노드의 prev가 되고
            # 새로운 tail은 새로추가한 노드가 된다.
            # 새로운 노드가 맨 뒤에 추가되었으므로
            # 새로 추가된 노드의 next는 None이다.
            self.tail = Node(value, before_tail, None)
            # 이전 tail의 다음을 현재 tail로 바꿔준다.
            before_tail.next = self.tail
            # 맨 뒤에 추가했으므로 self.head 은 바뀌지 않는다.

    def set_head(self, index):
        if self.is_empty():
            print("Out of Range")
            return False

        # head부터 시작해서
        curr = self.head
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            curr = curr.next
        self.head = curr
        # 이제 curr가 맨 앞 노드가 되었으니
        # curr의 prev를 None으로 해준다.
        curr.prev = None
        return True

    def access(self, index):
        if self.is_empty():
            print("Out of Range")
            return False
        # head부터 시작해서
        curr = self.head
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            curr = curr.next
        if curr is None:
            # 범위가 벗어났음을 알리는 error 출력
            print("Out of Range")
            return False
        else:
            return curr.value

    def insert(self, index, value):
        if self.is_empty() and index > 0:
            print("Out of Range")
            return False
        if index == 0:
            self.prepend(value)
            return True
        # head부터 시작해서
        curr = self.head
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            curr = curr.next
        # 맨 마지막 삽입 = append와 동일
        if curr is None:
            # 현재 curr를 next로
            # 현재 curr의 prev가 가리키던걸 prev로
            # 새 노드는 이전 tail의 다음에 넣어준다.
            before_tail = self.tail
            before_tail.next = Node(value, curr.prev, curr)
            self.tail = before_tail.next
        else:
            before_node = curr.prev
            after_node = curr
            before_node.next = Node(value, before_node, after_node)
        return True

    def remove(self, index):
        if self.is_empty():
            print("Out of Range")
            return False
        if index == 0:
            self.head = self.head.next
            # self.head가 None이 아니라면
            if self.head is not None:
                # 이제 맨 앞이므로 prev를 None으로 해줘야 한다.
                self.head.prev = None
            return True
        # head부터 시작해서
        curr = self.head
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            curr = curr.next
        if curr is None:
            return False
        else:
            before_node = curr.prev
            after_node = curr.next
            before_node.next = after_node
            # after_node 가 None이면
            if after_node is None:
                # tail을 before_node로 바꿔줘야한다.
                # before_node가 마지막 노드이므로
                self.tail = before_node
            # None이 아니면
            else:
                # 앞의 노드를 가리켜준다.
                after_node.prev = before_node

    def print(self):
        print('[', end='')
        curr = self.head
        while curr is not None:
            print(curr.value, end='')
            if curr.next is not None:
                print(", ", end='')
            curr = curr.next
        print(']')


print("---------------Test Code---------------")
# 더블 링크드 리스트 생성
print("1. 더블 링크드 리스트 생성")
myDoublyLinkedList = DoublyLinkedList()
myDoublyLinkedList.print()
print("---------------------------------------")

# 더블 링크드 리스트가 비어있는 지 확인
print("2.더블 링크드 리스트가 비어있는 지 확인")
print(myDoublyLinkedList.is_empty())
myDoublyLinkedList.print()
print("---------------------------------------")

# 더블 링크드 리스트의 맨 앞에 요소를 삽입
print("3.더블 링크드열 리스트의 맨 앞에 요소 1을 삽입")
myDoublyLinkedList.prepend(1)
myDoublyLinkedList.print()
print("---------------------------------------")

print("4.더블 링크드 리스트의 맨 앞에 요소 2을 삽입")
myDoublyLinkedList.prepend(2)
myDoublyLinkedList.print()
print("---------------------------------------")

# 더블 링크드 리스트의 맨 뒤에 요소를 삽입
print("5. 더블 링크드 리스트의 맨 뒤에 요소 3를 삽입")
myDoublyLinkedList.append(3)
myDoublyLinkedList.print()
print("---------------------------------------")

# 더블 링크드 리스트의 맨 뒤에 요소를 삽입
print("6. 더블 링크드 리스트의 맨 뒤에 요소 4를 삽입")
myDoublyLinkedList.append(4)
myDoublyLinkedList.print()
print("---------------------------------------")

# 더블 링크드 리스트의 첫 머리를 변경
print("7. 더블 링크드 리스트의 첫 머리를 index 1 로 변경")
myDoublyLinkedList.set_head(1)
myDoublyLinkedList.print()
print("---------------------------------------")

# 주어진 인덱스의 해당 요소에 접근
print("8. 인덱스 2 에 접근")
# 4
print(myDoublyLinkedList.access(2))
print("---------------------------------------")

# 주어진 인덱스에 새로운 요소 삽입
print("9. 인덱스 2 에 새로운 요소 5 삽입")
myDoublyLinkedList.insert(2, 5)
myDoublyLinkedList.print()
print("---------------------------------------")

# 주어진 인덱스에 해당하는 요소를 제거
print("10. 인덱스 1에 있는 요소 삭제")
myDoublyLinkedList.remove(1)
myDoublyLinkedList.print()
print("---------------------------------------")

print("!!! 매개 변수로 index를 받는 함수들의 경우 - Out of Range Error 체크!!!\n")

# 더블 링크드 리스트의 첫 머리를 변경
print("12. 더블 링크드 리스트의 첫 머리를 인덱스 범위를 벗어나는 index 6 로 변경하려 시도")
myDoublyLinkedList.set_head(6)
myDoublyLinkedList.print()
print("---------------------------------------")
# 인덱스 범위를 벗어나는 요소 접근
print("13. 인덱스 범위를 벗어나는 index 5에 접근 시도")
print(myDoublyLinkedList.access(5))
myDoublyLinkedList.print()
print("---------------------------------------")

# 범위를 벗어난 인덱스에 새로운 요소 삽입 시도
print("14. 인덱스 7 에 새로운 요소 100 삽입 시도")
myDoublyLinkedList.insert(7, 100)
myDoublyLinkedList.print()
print("---------------------------------------")

# 범위를 벗어난 인덱스에 해당하는 요소를 제거 시도
print("15. 인덱스 4에 있는 요소 삭제 시도")
myDoublyLinkedList.remove(4)
myDoublyLinkedList.print()
