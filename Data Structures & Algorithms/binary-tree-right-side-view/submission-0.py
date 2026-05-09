# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        res = []
        if root:
            que.append(root)
        
        while len(que) > 0:
            layer = []
            for _ in range(len(que)):
                cur = que.popleft()
                layer.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            res.append(layer)
        return [last_val[-1] for last_val in res]
