from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, prev):
            visit[node] = True
            for nei in adj[node]:
                if nei != prev and not visit[nei]:
                    dfs(nei, node)
        
        visit = [False] * n
        res = 0
        for i in range(n):
            if not visit[i]:
                dfs(i, -1)
                print(visit)
                res += 1
        
        return res