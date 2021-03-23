import array


class ArrayList:
    # 배열 리스트 생성
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
        return True
        # 타입코드 l 은 파이썬에서 int, byte 4
        # capacity 만큼 0을 할당

    # 배열 리스트가 비어있는 지 확인
    def is_empty(self):
        return self.length == 0

    # 배열 리스트의 맨 앞에 개체를 삽입
    def prepend(self, value):
        # 배열 리스트가 꽉 차있어 새로운 요소를 넣을 수 없다면
        # = 배열 리스트의 용량과 배열 리스트의 길이가 같다.
        if self.capacity == self.length:
            # 그 크기의 2배의 새 배열 리스트를 새로 생성
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            # 새로운 값을 맨 앞에 삽입
            new_array[0] = value
            # 원래 배열 리스트의 모든 요소를
            # 새로운 값 뒤에 넣어준다.
            for i in range(self.length):
                new_array[i+1] = self.array[i]
            # 원래 배열 주소에 새로운 배열 주소를 넣어준다.
            self.array = new_array
        # 배열 리스트에 빈 자리가 있다면
        else:
            # 배열 리스트의 모든 요소를 한 칸씩 밀어준다.
            # 이 때, 원래 값이 사라지지 않도록 맨 뒤에서 부터 밀어준다.
            for i in range(self.length-1, -1, -1):
                self.array[i+1] = self.array[i]
            self.array[0] = value
        # 삽입이 끝났다면 length를 하나 더해준다.
        self.length += 1
        return True

    # 리스트의 맨 뒤에 개체를 삽입
    def append(self, value):
        # 배열 리스트가 꽉 차있어 새로운 요소를 넣을 수 없다면
        #  = 배열 리스트의 용량과 배열 리스트의 길이가 같다.
        if self.capacity == self.length:
            # 2배 크기의 새 배열 리스트 할당
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)

            # 이전 배열 리스트의 모든 요소를
            # 새 배열 리스트에 복사
            for i in range(self.length):
                new_array[i] = self.array[i]
            # 맨 뒤에 새로운 요소 추가
            new_array[self.length] = value
        else:
            # 맨 뒤에 새로운 요소 추가
            self.array[self.length] = value
        self.length += 1
        return True

    def set_head(self, index):
        # 접근할 수 없는 index라면
        if(index >= self.length):
            # 범위를 벗어났다는 error를 띄운다.
            print("Out of Range!!!")
            return False
        # 해당 인덱스 이전을 슬라이싱으로 잘라
        # 해당 인덱스부터 맨 뒤까지의 요소만 남긴다.
        self.array = self.array[index:]
        # 해당 인덱스 앞까지 사라졌으므로
        # 용량도 그만큼 빼주고
        self.capacity = self.capacity - index
        # 길이도 그만큼 빼준다.
        self.length = self.length - index
        return True

    def access(self, index):
        # 접근할 수 없는 index라면
        if(index >= self.length):
            # 범위를 벗어났다는 error를 띄운다.
            return "Out of Range!!!"
        return self.array[index]

    def insert(self, index, value):
        # insert 는 index = self.length 인 경우에도 가능하므로
        # = 맨 뒤의 삽입이니까
        # index > self.length 인 경우에 범위를 벗어났다는 error를 띄운다.
        if(index > self.length):
            print("Out of Range!!!")
            return False
        # 배열 리스트가 꽉 차있어 새로운 요소를 넣을 수 없다면
        #  = 배열 리스트의 용량과 배열 리스트의 길이가 같다.
        if self.capacity == self.length:
            # 2배 크기의 새 배열 리스트 할당
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            # 삽입하고자 하는 인덱스 앞까지의 요소는
            # 새 배열 리스트에 그대로 복사한다.
            for i in range(index):
                new_array[i] = self.array[i]
            # 새로운 값을 해당 인덱스에 삽입한다.
            new_array[index] = value
            # 원래 배열 리스트의 나머지를
            # 삽입한 인덱스 뒤에 복사한다.
            for i in range(index+1, self.length+1):
                new_array[i] = self.array[i-1]
            # 원래 배열 주소에 새로운 배열 주소를 넣어준다.
            self.array = new_array
        else:
            for i in range(self.length, index, -1):
                self.array[i] = self.array[i-1]

            # 옆으로 밀어서 생긴 자리에 새로운 값을 삽입한다.
            self.array[index] = value
        self.length += 1
        return True

    def remove(self, index):
        # 접근할 수 없는 index라면
        if(index >= self.length):
            # 범위를 벗어났다는 error를 띄운다.
            print("Out of Range!!!")
            return False
        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]
        self.length -= 1
        return True

    # 배열 리스트 전체 출력
    def print(self):
        print('[', end="")
        for i in range(self.length):
            print(self.array[i], end="")
            if i != self.length-1:
                print(", ", end="")
        print('] ( Array Length :', self.length, ')')
        return True


print("---------------Test Code---------------")
# 배열 리스트 생성
print("1. 배열 리스트 생성")
myArrayList = ArrayList(10)
# array('l', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
myArrayList.print()
print("---------------------------------------")

# 배열 리스트가 비어있는 지 확인
print("2.배열 리스트가 비어있는 지 확인")
# True
myArrayList.print()
print("---------------------------------------")

# 배열 리스트의 맨 앞에 요소를 삽입
print("3.배열 리스트의 맨 앞에 요소 1을 삽입")
myArrayList.prepend(1)
# array('l', [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
myArrayList.print()
print("---------------------------------------")

print("4.배열 리스트의 맨 앞에 요소 2을 삽입")
myArrayList.prepend(2)
# array('l', [2, 1, 0, 0, 0, 0, 0, 0, 0, 0])
myArrayList.print()
print("---------------------------------------")

# 배열 리스트의 맨 뒤에 요소를 삽입
print("5. 배열 리스트의 맨 뒤에 요소 3를 삽입")
myArrayList.append(3)
# array('l', [2, 1, 3, 0, 0, 0, 0, 0, 0, 0])
myArrayList.print()
print("---------------------------------------")

# 배열 리스트의 맨 뒤에 요소를 삽입
print("6. 배열 리스트의 맨 뒤에 요소 4를 삽입")
myArrayList.append(4)
# array('l', [2, 1, 3, 4, 0, 0, 0, 0, 0, 0])
myArrayList.print()
print("---------------------------------------")

# 배열 리스트의 첫 머리를 변경
print("7. 배열 리스트의 첫 머리를 index 1 로 변경")
myArrayList.set_head(1)
# array('l', [1, 3, 4, 0, 0, 0, 0, 0, 0])
myArrayList.print()
print("---------------------------------------")

# 주어진 인덱스의 해당 요소에 접근
print("8. 인덱스 2 에 접근")
# 4
print(myArrayList.access(2))
print("---------------------------------------")

# 주어진 인덱스에 새로운 요소 삽입
print("9. 인덱스 2 에 새로운 요소 5 삽입")
myArrayList.insert(2, 5)
# array('l', [1, 3, 5, 4, 0, 0, 0, 0, 0])
myArrayList.print()
print("---------------------------------------")

# 주어진 인덱스에 해당하는 요소를 제거
print("10. 인덱스 1에 있는 요소 삭제")
myArrayList.remove(1)
myArrayList.print()
print("\n10.의 경우, \n완전히 잘 지워진 것처럼 보이지만\n메모리를 보면")
print(myArrayList.array, "로")
print("\nlength보다 커서 length로 접근하지 못하는 곳에는 \n아직 4라는 값이 남아있다.")

# 맨 뒤에 삽입하는 경우
print("\n이는 맨 뒤에 삽입하면 덮어씌워져 사라지므로 문제 없다.\n")
print("11. 맨 뒤에 요소 10 을 삽입하면")
myArrayList.append(10)
myArrayList.print()
print("위와 같이 length로 접근하는 것도 문제없고")

print("\n메모리를 봐도 아래와 같이 잘 덮어씌워진 걸 볼 수 있다.")
print(myArrayList.array)
print("---------------------------------------")

print("!!! 매개 변수로 index를 받는 함수들의 경우 - Out of Range Error 체크!!!\n")

# 배열 리스트의 첫 머리를 변경
print("12. 배열 리스트의 첫 머리를 인덱스 범위를 벗어나는 index 6 로 변경하려 시도")
myArrayList.set_head(6)
myArrayList.print()
print("---------------------------------------")
# 인덱스 범위를 벗어나는 요소 접근
print("13. 인덱스 범위를 벗어나는 index 5에 접근 시도")
print(myArrayList.access(5))
myArrayList.print()
print("---------------------------------------")

# 범위를 벗어난 인덱스에 새로운 요소 삽입 시도
print("14. 인덱스 7 에 새로운 요소 100 삽입 시도")
myArrayList.insert(7, 100)
myArrayList.print()
print("---------------------------------------")

# 범위를 벗어난 인덱스에 해당하는 요소를 제거 시도
print("15. 인덱스 4에 있는 요소 삭제 시도")
myArrayList.remove(4)
myArrayList.print()
