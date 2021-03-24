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
            return True

    def pop(self):
        if self.top == 0:
            print("Stack UnderFlow")
            return False
        else:
            topValue = self.array[self.top-1]
            self.array = self.array[:self.top - 1]
            return topValue

    def peek(self):
        return self.top

    def is_empty(self):
        return self.top == 0

    def print(self):
        print("| ", end='')
        while self.top >= 0:
            print(self.pop(), end=' |\n')
            print('__')


myStack = Stack(10)
print(myStack.peek())
