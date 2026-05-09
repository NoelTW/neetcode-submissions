# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = root
        curr_val = -float("inf")
        ans = True
        def dfs(root):
            nonlocal curr_val
            nonlocal ans
            if not root:
                return 
            dfs(root.left)
            if root.val <= curr_val:
                ans = False
            curr_val = root.val
            dfs(root.right)
        dfs(root)
        return ans
        
                
            