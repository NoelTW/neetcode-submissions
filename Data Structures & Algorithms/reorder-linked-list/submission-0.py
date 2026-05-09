class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: 找中間點
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: 反轉後半部
        second = slow.next
        slow.next = None  # 斷開前半部和後半部
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Step 3: 合併兩半
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
