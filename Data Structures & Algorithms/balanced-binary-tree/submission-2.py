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
                return 0, True
            lh, l_res = dfs(root.left)
            rh, r_res = dfs(root.right)
            mh = max(lh, rh)
            is_balanced = l_res and r_res and abs(lh- rh) <= 1
            return mh + 1, is_balanced
        return dfs(root)[1]