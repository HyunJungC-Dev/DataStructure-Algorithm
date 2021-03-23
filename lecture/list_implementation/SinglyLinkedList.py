class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    # 싱글 링크드 리스트 생성
    def __init__(self):
        self.head = None

    # 싱글 링크드 리스트가 비어있는 지 확인
    def is_empty(self):
        # head 가 None 이면 링크드리스트에 아무것도 없는 것이다.
        return self.head is None

    # 싱글 링크드 리스트의 맨 앞에 요소 추가
    def prepend(self, value):
        # 싱글 링크드 리스트가 비어있다면
        if self.is_empty():
            # 뒤를 가리키는 next엔 None이 들어간다.
            self.head = Node(value, None)
        # 싱글 링크드 리스트에 다른 요소가 있다면
        else:
            # 원래 head가
            before_head = self.head
            # 새로 맨 앞에 추가한 노드의 next가 되고
            # 새로 추가한 노드의 주소가 새 head가 된다.
            self.head = Node(value, before_head)

    # 싱글 링크드 리스트 맨 뒤에 요소 추가
    def append(self, value):
        # 싱글 링크드 리스트가 비어있다면
        if self.is_empty():
            # 비어있을 때 맨 앞에 추가하는 것과 동일하다.
            self.head = Node(value, None)
        else:
            # head부터 시작해서
            curr = self.head
            # curr의 next를 쭉 타고 next가 None 일 때까지
            # curr를 옮긴다.
            while curr.next is not None:
                curr = curr.next
            # 현재 curr.next는 None 이므로
            # 이 curr.next에 새로운 노드의 주소를 추가해줘야한다.
            # 새로운 노드느 맨 마지막 노드이므로 next는 None이다.
            curr.next = Node(value, None)
        return True

    # 주어진 index를 head로 결정
    def set_head(self, index):
        # 애초에 싱글 리크드 리스트가 비어있으면 불가능한 작업
        if self.is_empty():
            return False
        # 원래 head부터 시작해서
        curr = self.head
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            curr = curr.next
        self.head = curr
        return True

    def access(self, index):
        # 애초에 싱글 리크드 리스트가 비어있으면 불가능한 작업
        if self.is_empty():
            return False
        # 원래 head부터 시작해서
        curr = self.head
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            curr = curr.next
        return curr.value

    def insert(self, index, value):
        curr = self.head
        before_node = None
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            before_node = curr
            curr = curr.next
        # 현재 curr 가 이제 새로운 노드의 next에 주소가 되고
        # 현재 curr 이전의 before_node의 next에 주소가 새로운 노드의 주소가 된다.
        before_node.next = Node(value, curr)
        return True

    def remove(self, index):
        # 애초에 싱글 리크드 리스트가 비어있으면 불가능한 작업
        if self.is_empty():
            return False
        curr = self.head
        before_node = None
        for i in range(index):
            # 만약 index 만큼의 요소가 존재하지 않다면
            if curr is None:
                # 범위가 벗어났음을 알리는 error 출력
                print("Out of Range")
                return False
            before_node = curr
            curr = curr.next
        if curr is None:
            return False
        # 현재 curr 가 없어질 노드이므로
        # 현재 curr 이전의 before_node의 next에 주소가
        # 현재 curr의 next의 주소가 된다.
        before_node.next = curr.next
        return True

    def print(self):
        curr = self.head
        print('[', end='')
        while curr is not None:
            print(curr.value, end='')
            if curr.next is not None:
                print(', ', end='')
            curr = curr.next
        print(']')


print("---------------Test Code---------------")
# 싱글 링크드 리스트 생성
print("1. 싱글 링크드 리스트 생성")
mySinglyLinkedList = SinglyLinkedList()
mySinglyLinkedList.print()
print("---------------------------------------")

# 싱글 링크드 리스트가 비어있는 지 확인
print("2.싱글 링크드 리스트가 비어있는 지 확인")
mySinglyLinkedList.is_empty()
mySinglyLinkedList.print()
print("---------------------------------------")

# 싱글 링크드 리스트의 맨 앞에 요소를 삽입
print("3.싱글 링크드열 리스트의 맨 앞에 요소 1을 삽입")
mySinglyLinkedList.prepend(1)
mySinglyLinkedList.print()
print("---------------------------------------")

print("4.싱글 링크드 리스트의 맨 앞에 요소 2을 삽입")
mySinglyLinkedList.prepend(2)
mySinglyLinkedList.print()
print("---------------------------------------")

# 싱글 링크드 리스트의 맨 뒤에 요소를 삽입
print("5. 싱글 링크드 리스트의 맨 뒤에 요소 3를 삽입")
mySinglyLinkedList.append(3)
mySinglyLinkedList.print()
print("---------------------------------------")

# 싱글 링크드 리스트의 맨 뒤에 요소를 삽입
print("6. 싱글 링크드 리스트의 맨 뒤에 요소 4를 삽입")
mySinglyLinkedList.append(4)
mySinglyLinkedList.print()
print("---------------------------------------")

# 싱글 링크드 리스트의 첫 머리를 변경
print("7. 싱글 링크드 리스트의 첫 머리를 index 1 로 변경")
mySinglyLinkedList.set_head(1)
mySinglyLinkedList.print()
print("---------------------------------------")

# 주어진 인덱스의 해당 요소에 접근
print("8. 인덱스 2 에 접근")
# 4
print(mySinglyLinkedList.access(2))
print("---------------------------------------")

# 주어진 인덱스에 새로운 요소 삽입
print("9. 인덱스 2 에 새로운 요소 5 삽입")
mySinglyLinkedList.insert(2, 5)
mySinglyLinkedList.print()
print("---------------------------------------")

# 주어진 인덱스에 해당하는 요소를 제거
print("10. 인덱스 1에 있는 요소 삭제")
mySinglyLinkedList.remove(1)
mySinglyLinkedList.print()
print("---------------------------------------")

print("!!! 매개 변수로 index를 받는 함수들의 경우 - Out of Range Error 체크!!!\n")

# 싱글 링크드 리스트의 첫 머리를 변경
print("12. 싱글 링크드 리스트의 첫 머리를 인덱스 범위를 벗어나는 index 6 로 변경하려 시도")
mySinglyLinkedList.set_head(6)
mySinglyLinkedList.print()
print("---------------------------------------")
# 인덱스 범위를 벗어나는 요소 접근
print("13. 인덱스 범위를 벗어나는 index 5에 접근 시도")
print(mySinglyLinkedList.access(5))
mySinglyLinkedList.print()
print("---------------------------------------")

# 범위를 벗어난 인덱스에 새로운 요소 삽입 시도
print("14. 인덱스 7 에 새로운 요소 100 삽입 시도")
mySinglyLinkedList.insert(7, 100)
mySinglyLinkedList.print()
print("---------------------------------------")

# 범위를 벗어난 인덱스에 해당하는 요소를 제거 시도
print("15. 인덱스 4에 있는 요소 삭제 시도")
mySinglyLinkedList.remove(4)
mySinglyLinkedList.print()
