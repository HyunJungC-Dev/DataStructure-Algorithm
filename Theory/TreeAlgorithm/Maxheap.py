class MaxHeap:
    def __init__(self):
        self.arr = [None]

    def push(self, val):
        self.arr.append(val)
        if len(self.arr)-1 == 1:
            return
        else:
            parent_idx = (len(self.arr)-1)//2
            val_idx = (len(self.arr)-1)
            while parent_idx:
                if self.arr[parent_idx] < self.arr[val_idx]:
                    self.arr[parent_idx],  self.arr[val_idx] = self.arr[val_idx], self.arr[parent_idx]
                    val_idx = parent_idx
                    parent_idx = val_idx//2
                else:
                    break
            return

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

myMH = MaxHeap()
myMH.push(1)
myMH.push(2)
myMH.push(3)
myMH.push(4)
myMH.push(7)
myMH.push(5)
print(myMH.arr)
