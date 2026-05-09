class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        
        graph = {}

        for src, dst in edges:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)
            graph[dst].append(src)
    

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        state = [UNVISITED] * n
        def dfs(node, prev):
            if  state[node] == 1:
                return False
            elif  state[node] == 2:
                return True
            state[node] = VISITING
            for next_node in graph[node]:
                if next_node == prev:
                    continue
                if not dfs(next_node, node):
                    return False
            state[node] = VISITED
            return True

        res = dfs(0, -1) and (sum(state) // 2) == n
        return res
 
