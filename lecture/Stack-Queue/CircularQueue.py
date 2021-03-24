import array


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        self.array[self.rear] = value
        self. rear = (self.rear + 1) % self.capacity

    def get(self):
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        return value

    def peek(self):
        return self.array[self.front]

    def print(self):
        pass


myCircularQueue = CircularQueue(10)
