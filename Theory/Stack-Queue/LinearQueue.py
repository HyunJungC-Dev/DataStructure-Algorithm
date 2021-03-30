import array


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            print("Overflow")
            return False
        self.array[self.rear] = value
        self.rear += 1
        return True

    def get(self):
        if self.front == self.rear:
            print("Underflow")
            return None
        get_value = self.array[self.front]
        self.front += 1
        return get_value

    def peek(self):
        if self.front == self.rear:
            print("Underflow")
            return None
        return self.array[self.front]

    def print(self):
        start = self.front
        end = self.rear
        print("<- ", end='')
        for i in range(start, end):
            print(self.array[i],end=' ')
        print("<- ", end='')
        print()

myLinearQueue = LinearQueue(3)
myLinearQueue.peek()
myLinearQueue.print()
myLinearQueue.get()
myLinearQueue.print()
myLinearQueue.put(1)
myLinearQueue.print()
myLinearQueue.put(2)
myLinearQueue.print()
myLinearQueue.put(3)
myLinearQueue.print()
myLinearQueue.put(4)
myLinearQueue.print()
print(myLinearQueue.get())
myLinearQueue.print()
print(myLinearQueue.get())
myLinearQueue.print()
myLinearQueue.put(4)
myLinearQueue.print()
