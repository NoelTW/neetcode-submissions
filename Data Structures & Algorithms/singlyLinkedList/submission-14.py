class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node(val={self.val}, next={self.next})"

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0 
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1 # index out of bound

    def insertHead(self, val: int) -> None:
        new_node = Node(val=val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        print(self.head.next)
        
    def insertTail(self, val: int) -> None:
        new_node = Node(val=val)
        self.tail.next = new_node
        self.tail = new_node
                
        print(self.head.next)

    def remove(self, index: int) -> bool:
        prev = self.head
        i = 0
        while i < index and prev:
            i += 1
            prev = prev.next
        if prev and prev.next:
            if prev.next == self.tail:
                self.tail = prev
            prev.next = prev.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        vals = []
        while curr:
            vals.append(curr.val)   
            curr = curr.next
        return vals
