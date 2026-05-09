class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        ans = 0
        for i in range(n):
            start_j = i
            while stack and heights[i] < stack[-1][1]:
                j, h = stack.pop()
                start_j = j
                w = i- j 
                ans = max(ans, w * h)
            stack.append((start_j, heights[i]))
        while stack:
            j, h = stack.pop()
            w = n - j
            ans = max(w* h, ans)
        return ans
                