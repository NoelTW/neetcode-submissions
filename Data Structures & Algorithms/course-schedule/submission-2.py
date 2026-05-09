class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        
        for src, dst in prerequisites:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)

        VISITED = 2
        VISITING = 1
        UNVISITED = 0
        state = [UNVISITED] * numCourses

        def dfs(node) -> bool:            
            if state[node] == VISITING:
                return False
            elif state[node] == VISITED:
                return True
            state[node] = VISITING
            if node not in graph:
                return True
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False
            state[node] = VISITED
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
