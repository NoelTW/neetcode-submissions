# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        # reverse the second half
        def reverse_list(head):
            prev= 0 
            curr= head
            while curr:
                temp = curr.next
                curr.next = prev
                prev, curr = curr , temp
            return prev
        b = reverse_list(s.next)
        a = head
        s.next =None
        def merge_list(a,b):
            dummy = ListNode()
            tail = dummy
            while a and b:
                tail.next = a
                a = a.next
                tail = tail.next
                tail.next = b
                b = b.next
                tail = tail.next
            tail.next = a or b
        merge_list(a,b )







