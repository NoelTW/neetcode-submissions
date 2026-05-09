# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        curr_1 = list1
        curr_2 = list2
        while curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                curr.next = curr_1
                curr_1 = curr_1.next
            else:
                curr.next = curr_2
                curr_2 = curr_2.next
            curr = curr.next
        curr.next = curr_2 if curr_2 else curr_1
        
        return dummy.next