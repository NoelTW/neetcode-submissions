# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subRoot):
            if not root:
                return False
            if root.val == subRoot.val and check(root, subRoot):
                return True
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        def check(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            return check(root.left, subRoot.left) and check(root.right, subRoot.right) and root.val == subRoot.val
        
        return dfs(root, subRoot)
            