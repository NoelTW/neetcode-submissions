class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0 

    def append(self, value: int) -> None:
        new_node = Node(value)
        # Connect to old prev
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        # attach to tail
        new_node.next = self.tail
        self.tail.prev = new_node
        self.length += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        # Connect to old next
        new_node.next = self.head.next
        self.head.next.prev = new_node
        # attach to head
        self.head.next = new_node
        new_node.prev = self.head
        self.length += 1 

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        value = self.tail.prev.value
        # Remove the last node
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.length -= 1
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.next.value
        # Remove the first node
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.length -= 1
        return value
        
