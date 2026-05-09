from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        que = deque([])
        ans = []
        for r in range(n):
            while que and nums[r] >= nums[que[-1]]:
                que.pop()
            if que and r - que[0] + 1 > k:
                que.popleft()
            que.append(r)
            if r >= k - 1:
                ans.append(nums[que[0]])
        return ans
        