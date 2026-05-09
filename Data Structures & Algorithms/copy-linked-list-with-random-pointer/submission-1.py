"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = {None:None}
        # first pass
        curr = head
        while curr:
            new_node = Node(x=curr.val)
            table[curr] = new_node
            curr = curr.next
        
        # second pass
        curr = head
        while curr:
            new_node = table[curr]
            new_node.next = table[curr.next]
            new_node.random = table[curr.random]
            curr = curr.next
        return table[head]
        

                    