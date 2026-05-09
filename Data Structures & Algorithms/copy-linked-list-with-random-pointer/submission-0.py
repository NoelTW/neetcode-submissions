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
        old_2_new = {None : None}

        curr = head
        while curr:
            old_2_new[curr] = Node(x=curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_2_new[curr].next = old_2_new[curr.next]
            old_2_new[curr].random = old_2_new[curr.random]
            curr = curr.next
        
        return old_2_new[head]