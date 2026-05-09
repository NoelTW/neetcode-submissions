# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head.next
        
        while f:
            if f == s:
                return True
            if not f.next:
                return False
            s = s.next
            f = f.next.next
        return False
