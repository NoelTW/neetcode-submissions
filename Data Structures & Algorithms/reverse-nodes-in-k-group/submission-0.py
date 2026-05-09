# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def find_kth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:

            # find kth
            kth = find_kth(group_prev, k)
            if not kth:
                break
            # start reverse
            prev, curr = kth.next, group_prev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Update links
            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp

        return dummy.next

