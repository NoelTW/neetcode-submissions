# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        s, f = dummy, head
        i = 0
        while f and i < n:
            f = f.next
            i += 1
        while f:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy.next
    