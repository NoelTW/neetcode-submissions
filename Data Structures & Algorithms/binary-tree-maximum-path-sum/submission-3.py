# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        def dfs(root):
            if not root:
                return 0
            
            l_res = dfs(root.left)
            r_res = dfs(root.right)
            l_res = max(l_res, 0)
            r_res = max(r_res, 0)

            # non split

            self.res = max(self.res, l_res + r_res + root.val)

            return root.val + max(l_res, r_res)
        
        dfs(root)

        return self.res
