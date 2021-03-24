import array


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.isFull = False
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        # is 면 True 일 때만, is True 빼면 1일 때도, 리스트에 값이 있을 때도 존재한다.
        if self.isFull is True:
            print("Overflow")
            return False

        self.array[self.rear] = value
        self. rear = (self.rear + 1) % self.capacity

        if self.rear == self.front:
            self.isFull = True
        return True

    def get(self):
        if self.isFull is False and self.front == self.rear:
            print("Underflow")
            return None
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.isFull = False
        return value

    def peek(self):
        if self.isFull is False and self.front == self.rear:
            print("Underflow")
            return None

        return self.array[self.front]

    def print(self):
        curr = self.front
        if self.isFull is True:
            print(self.array[curr], end=' ')
            curr = (curr+1) % self.capacity
            while curr != self.rear:
                print(self.array[curr], end=' ')
                curr = (curr+1) % self.capacity

        else:
            while curr != self.rear:
                print(self.array[curr])
                curr = (curr+1) % self.capacity


myCircularQueue = CircularQueue(5)
myCircularQueue.put(10)
myCircularQueue.put(20)
myCircularQueue.put(30)
myCircularQueue.put(40)
myCircularQueue.put(50)
myCircularQueue.get()
myCircularQueue.get()
myCircularQueue.get()
myCircularQueue.get()
myCircularQueue.get()
myCircularQueue.put(60)
myCircularQueue.put(70)
myCircularQueue.put(80)
myCircularQueue.put(90)
myCircularQueue.put(100)
print(myCircularQueue.array)
myCircularQueue.print()
