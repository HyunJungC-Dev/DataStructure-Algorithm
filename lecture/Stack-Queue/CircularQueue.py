import array


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            print("OverFlow")
            return False
        else:
            self.array[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            return True

    def get(self):
        if self.front > self.rear:
            return False
        else:
            get_value = self.array[self.front]
            self.front = (self.front+1) % self.capacity
            return get_value

    def peek(self):
        return self.array[self.front]

    def print(self):
        print("<-", end='')
        curr = self.front
        while curr < self.rear:
            print(self.array[curr], end=' ')
            curr += 1
        print("<-", end='')
        print(" ( Capacity : ", self.capacity, ")")


myCircularQueue = CircularQueue(10)

print("1. Queue에 10 삽입")
myCircularQueue.put(10)
print(myCircularQueue.array)
myCircularQueue.print()
print("---------------------------------------")

print("2. Queue에 20 삽입")
myCircularQueue.put(20)
print(myCircularQueue.array)
myCircularQueue.print()
print("---------------------------------------")

print("3. Queue에서 peek")
print(myCircularQueue.peek())
print(myCircularQueue.array)
myCircularQueue.print()
print("---------------------------------------")

print("4. Queue에서 get")
print(myCircularQueue.get())
print(myCircularQueue.array)
myCircularQueue.print()
print("---------------------------------------")
