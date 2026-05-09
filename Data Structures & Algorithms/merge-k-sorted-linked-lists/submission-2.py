# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_lists(li1, li2):
            dummy = ListNode()
            curr = dummy
            c1, c2 = li1, li2
            while c1 and c2:
                if c1.val < c2.val:
                    curr.next = c1
                    c1 = c1.next
                else:
                    curr.next = c2
                    c2 = c2.next
                curr = curr.next
            curr.next = c1 or c2
            return dummy.next
        dummy = ListNode(val=-float("inf"))
        curr = dummy
        for i in range(len(lists)):
            curr = merge_lists(curr, lists[i])
        return dummy.next








                    