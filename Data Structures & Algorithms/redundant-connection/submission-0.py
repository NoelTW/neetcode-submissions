class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        def dfs(src, dst, visit):
            if src not in graph:
                graph[src].append(dst)
                graph[dst].append(src)
                return False
            if src == dst:
                return True
            if src in visit:
                return False
            visit.add(src)  
            for next_node in graph[src]:
                res = dfs(next_node, dst, visit) 
                if res:
                    return True
            return False
        
        for src, dst in edges:
            if dfs(src, dst, set()):
                return [src, dst]
            graph[src].append(dst)
            graph[dst].append(src)
            
         
