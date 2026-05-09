# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        res = []
        if root:
            que.append(root)
        layer = 0
        while len( que ) > 0 :
            layer_list = []   
            for _ in range(len(que)):
                cur = que.popleft()
                layer_list.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

            res.append(layer_list)
        return res





        