class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        VISITING = 1
        VISITED = 2
        adj_list = {}
        # Create a adj_list
        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            if dst not in adj_list:
                adj_list[dst] = []
            adj_list[src].append(dst)

        # DFS
        visit = dict()
        def dfs(node):
            # base case
            if not adj_list[node]:
                return True

            if node in visit and visit[node] == 1:
                return False
            
            
            for next_node in adj_list[node]:
                if next_node in visit and visit[next_node] == 2:
                    continue
                visit[node] = 1
                res = dfs(next_node)
                if not res:
                    return res
                visit[node] = 2
            
            return True

        for node in prerequisites:
            if not dfs( node[0] ):
                return False
        
        return True