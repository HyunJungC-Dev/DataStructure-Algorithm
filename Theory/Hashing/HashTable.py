# dictionary 처럼 동작
class HashTable:
    def __init__(self, bucket_size, hash_func):
        self.bucket_size = bucket_size
        self.bucket = [[]]*self.bucket_size
        self.hash_func = hash_func

    def set(self, key, value):
        hash_value = self.hash_func(key)
        bucket_idx = hash_value % self.bucket_size
        if self.bucket[bucket_idx] == []:
            self.bucket[bucket_idx] = [key, value, None]
        else:
            curr = self.bucket[bucket_idx]
            while curr is not None:
                if curr[2] is None:
                    curr[2] = [key, value, None]
                    return True
                curr = curr[2]

    def get(self, key):
        hash_value = self.hash_func(key)
        bucket_idx = hash_value % self.bucket_size
        curr = self.bucket[bucket_idx]
        while curr is not None:
            if curr[0] == key:
                return key, curr[1]
            else:
                curr = curr[2]
        return False

    def print(self):
        print(self.bucket)


myht = HashTable(2, lambda x: x+2)
myht.set(1, 2)
myht.set(2, 3)
myht.set(3, 4)
myht.set(4, 5)
myht.set(4, 10)
myht.set(5, 6)
myht.set(6, 7)
myht.print()
print(myht.get(1))
print(myht.get(2))
print(myht.get(3))
print(myht.get(4))
print(myht.get(5))
print(myht.get(6))
