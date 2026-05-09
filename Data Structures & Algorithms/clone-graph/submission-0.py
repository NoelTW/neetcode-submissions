"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_2_new = {}
        
        def dfs(node):
            if node not in old_2_new:
                old_2_new[node] = Node(node.val)
                for next_node in node.neighbors:
                    dfs(next_node)
        dfs(node)

        for old, new in old_2_new.items():
            for old_next in old.neighbors:
                new.neighbors.append(old_2_new[old_next])
        
        return old_2_new[node]
            