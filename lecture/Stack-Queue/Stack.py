import array


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0]*capacity)

    def push(self, value):
        if self.top == self.capacity:
            print("Stack OverFlow")
            return False
        else:
            self.array[self.top] = value
            self.top += 1
            return True

    def pop(self):
        if self.top == 0:
            print("Stack UnderFlow")
            return False
        else:
            topValue = self.array[self.top-1]
            # self.array = self.array[:self.top - 1]
            # 어차피 top 으로 위쪽은 사용하지 않는다는 것을 알기 때문에!
            self.top -= 1
            return topValue

    def peek(self):
        if self.is_empty():
            return False
        return self.array[self.top-1]

    def is_empty(self):
        return self.top == 0

    def print(self):
        if self.is_empty():
            print("Stack is Empty")
            return True
        last_value = self.top - 1
        while last_value >= 0:
            print("| ", end='')
            print(self.array[last_value], end=' |\n')
            print('-----')
            last_value -= 1
        return True


myStack = Stack(10)
print("1. Stack 이 비어있는 지 확인")
print(myStack.is_empty())
myStack.print()

print("2. Stack 에 1 push")
print(myStack.push(1))
myStack.print()

print("3. Stack 에 7 push")
print(myStack.push(7))
myStack.print()

print("4. Stack 에 3 push")
print(myStack.push(3))
myStack.print()

print("5. Stack 에서 pop")
print("pop 된 값 : ", myStack.pop())
myStack.print()

print("6. Stack 에서 peek")
print("peek 된 값 : ", myStack.peek())
myStack.print()
