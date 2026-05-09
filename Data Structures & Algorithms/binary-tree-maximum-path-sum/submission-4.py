# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def dfs(root):
            if not root:
                return 0
            
            l_res = max( dfs(root.left), 0 )
            r_res = max( dfs(root.right), 0)
            nonlocal max_sum
            max_sum = max(max_sum,root.val + l_res + r_res)

            return root.val+ max(l_res, r_res, 0)

        dfs(root)
        return max_sum
            
