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
        old2new = {}
        seen = set()
        def dfs(node):
            if node in old2new:
                return 
            new_node = Node(node.val)
            old2new[node] = new_node
            for neighbor in node.neighbors:
                dfs(neighbor)
        def clone(node):
            if node in seen:
                return
            seen.add(node)
            old2new[node].neighbors = [old2new[neighbor] for neighbor in node.neighbors]
            for neighbor in node.neighbors:
                clone(neighbor)
        dfs(node)
        clone(node)
        return old2new[node]