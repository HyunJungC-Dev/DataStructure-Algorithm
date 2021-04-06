class HashTable:
    def __init__(self, hash_func=None, bucket_size=16):
        if hash_func is None:
            self.hash_func = hash
        else:
            self.hash_func = hash_func
        self.bucket_size = bucket_size
        self.bucket = [None]*bucket_size

    def set(self, key, value):
        hash_val = self. hash_func(key)
        bucket_index = hash_val % self.bucket_size

        node = self.bucket[bucket_index]
        if node is None:
            self.bucket[bucket_index] = [key, value, None]
            return True
        prev = None
        while node:
            if node[0] == key:
                node[1] = value
                return
            prev = node
            node = node[2]
        prev[2] = [key, value, None]

    def get(self, key):
        hash_val = self. hash_func(key)
        bucket_index = hash_val % self.bucket_size

        node = self.bucket[bucket_index]
        if node is None:
            return None
        prev = None
        while node:
            if node[0] == key:
                return node[1]
            prev = node
            node = node[2]
        return None
