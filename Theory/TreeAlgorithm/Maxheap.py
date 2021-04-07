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
        if self.is_empty():
            return None
        root_val = self.arr[1]
        replace_root_val = self.arr[-1]
        del self.arr[-1]
        self.arr[1] = replace_root_val
        root_idx = 1
        left_idx = 1*2
        right_idx = 1*2+1

        while root_idx <= len(self.arr)-1:
            if left_idx > len(self.arr)-1:
                break
            if right_idx > len(self.arr)-1:
                if self.arr[root_idx] < self.arr[left_idx]:
                    self.arr[root_idx], self.arr[left_idx] = self.arr[left_idx], self.arr[root_idx]
                else:
                    break
            if self.arr[root_idx] < self.arr[left_idx] or self.arr[root_idx] < self.arr[right_idx]:
                if self.arr[left_idx] < self.arr[right_idx]:
                    self.arr[root_idx], self.arr[right_idx] = self.arr[right_idx], self.arr[root_idx]
                    root_idx = right_idx
                else:
                    self.arr[root_idx], self.arr[left_idx] = self.arr[left_idx], self.arr[root_idx]
                    root_idx = left_idx

                left_idx = root_idx*2
                right_idx = root_idx*2+1
            else:
                break
        return root_val

    def peek(self):
        if self.is_empty():
            return None
        return self.arr[1]

    def is_empty(self):
        return len(self.arr)-1 == 1


myMH = MaxHeap()
myMH.push(1)
myMH.push(2)
myMH.push(3)
myMH.push(4)
myMH.push(7)
myMH.push(5)
print(myMH.arr)
myMH.pop()
print(myMH.arr)
