# Maitian order by doubly link list
# Store cache by hashmap

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        # Create lru and mru pointers (dummies)
        self.lru = Node(-1, -1)
        self.mru = Node(-1, -1)
        self.lru.next = self.mru
        self.mru.prev = self.lru
        

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.prev = self.mru.prev
        node.next = self.mru
        self.mru.prev.next = node
        self.mru.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node) # remove from list
            self.insert(node) # insert into most recently used
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
        else:
            node = Node(key, value)
            self.cache[key] = node
            if len(self.cache) > self.cap:
                # Remove the least recently used node
                lru_node = self.lru.next
                self.remove(lru_node)
                del self.cache[lru_node.key]
        self.insert(node)
        
        






        
