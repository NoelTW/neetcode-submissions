class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Define res array to store order
        res = []
        # globla vars
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        STATE = [UNVISITED] * numCourses
        # Create a graph
        graph = {}

        for src, dst in prerequisites:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)

        # Define DFS function
        def dfs(node: int ) -> bool:
            if STATE[node] == 1:
                return False
            if STATE[node] == 2:
                return True
            STATE[node] = VISITING
            if node not in graph:
                res.append(node)
                return True
            for next_node in graph[node]:
                if dfs(next_node) is False:
                    return False
            STATE[node] = VISITED
            res.append(node)
            
            return True


        # Call dfs
        for node in range(numCourses):
            if not dfs(node):
                return []
        return res