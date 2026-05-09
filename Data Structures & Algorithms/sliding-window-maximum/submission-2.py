class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # 存放 (索引, 值)，保证值单调递减
        res = []
        
        for i, x in enumerate(nums):
            # 1. 弹出窗口外的元素
            if q and q[0][0] <= i - k:
                q.popleft()
            
            # 2. 弹出所有比当前元素小的队尾元素
            while q and x >= q[-1][1]:
                q.pop()
            
            # 3. 将当前元素加入队尾
            q.append((i, x))
            
            # 4. i >= k-1 时，队首就是窗口最大值
            if i >= k - 1:
                res.append(q[0][1])
        
        return res
            