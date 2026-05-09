# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.distance = 0
        def dfs(root):
            if not root:
                return 0
            r_res = dfs(root.right)
            l_res = dfs(root.left)
            self.distance = max(self.distance, r_res + l_res)
            return max(r_res, l_res) + 1
        
        dfs(root) 

        return self.distance
        