class MyHashSet:

    def __init__(self):
        self.size = 2069
        self.hash_set = [[] for _ in range(self.size)]

    def _hash(self, val):
        hash_val = val % self.size
        return hash_val

    def add(self, key: int) -> None:
        hash_ = self._hash(key)
        bucket = self.hash_set[hash_]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        hash_ = self._hash(key)
        bucket = self.hash_set[hash_]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        hash_ = self._hash(key)
        return key in self.hash_set[hash_]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)