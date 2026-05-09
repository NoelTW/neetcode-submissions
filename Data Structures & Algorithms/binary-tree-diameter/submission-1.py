# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            l_res = dfs(root.left)
            r_res = dfs(root.right)
            ans = max(ans, l_res + r_res)
            return max(l_res, r_res) + 1
        dfs(root)
        return ans