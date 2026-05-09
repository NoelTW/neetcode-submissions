# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def check(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        # pre-order
        if root.val != subRoot.val:
            return False
        
        return self.check(root.left,subRoot.left) and self.check(root.right, subRoot.right)
    