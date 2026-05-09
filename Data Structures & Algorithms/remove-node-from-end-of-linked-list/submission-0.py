# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next = head)
        l = dummy
        # Setup right pointer
        r = dummy.next
        i = 0
        while i < n and r:
            r = r.next
            i += 1
        # Find answer (BC: r is None)
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next
             