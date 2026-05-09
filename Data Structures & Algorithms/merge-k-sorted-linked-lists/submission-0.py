# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, li in enumerate(lists):
            if li:
                heapq.heappush(heap, (li.val, i , li))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, li = heapq.heappop(heap)
            curr.next = ListNode(val)
            if li.next:
                heapq.heappush(heap, (li.next.val, i, li.next))
            curr = curr.next
        
        return dummy.next
