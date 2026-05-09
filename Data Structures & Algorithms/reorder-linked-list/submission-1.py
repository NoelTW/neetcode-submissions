# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid node
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
        prev = None
        curr = s.next
        # disjoin first and second bits and reverse second linked list
        s.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        f_head = head
        s_head = prev
        # join
        while s_head:
            s_temp = s_head.next
            f_temp = f_head.next
            f_head.next = s_head
            s_head.next = f_temp
            s_head = s_temp
            f_head = f_temp

