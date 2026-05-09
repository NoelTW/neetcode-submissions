from heapq import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hq = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            heappush(hq, -root.val)
            if len(hq) > k:
                heappop(hq)
            dfs(root.right)
        dfs(root)
        return -hq[0] if len(hq) == k else -1
