class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        visit = [UNVISITED] * n
        adj = {}
        
        for src, dst in prerequisites:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)
        
        def dfs(i):
            if visit[i] == VISITING:
                return False
            if visit[i] == VISITED:
                return True
            if i not in adj:
                return True
            
            visit[i] = VISITING
            for nei in adj[i]:
                res = dfs(nei)
                if not res:
                    return False
            visit[i] = VISITED
            return True

        for i in range(n):
            if visit[i] == UNVISITED:
                if not dfs(i):
                    print(visit)
                    return False
        
        return True
