import array


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        self.array[self.rear] = value
        self.rear += 1

    def get(self):
        get_value = self.array[self.front]
        self.front += 1
        return get_value

    def peek(self):
        return self.array[self.front]

    def print(self):
        pass
