class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h2 in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h2:
                j, h1 = stack.pop()
                max_area = max(max_area, h1 * (i - j))
                start = j
            stack.append([start, h2])
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
