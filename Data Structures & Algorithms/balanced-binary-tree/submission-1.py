# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0 
            # post
            l_res = dfs(root.left)
            r_res = dfs(root.right)

            if abs(l_res - r_res) > 1 or l_res == -1 or r_res == -1:
                return -1
            
            return max(l_res, r_res) + 1
        
        ans = dfs(root)
        return ans != -1