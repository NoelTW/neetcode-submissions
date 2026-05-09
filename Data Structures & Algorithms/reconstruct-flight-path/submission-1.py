class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        # create a adjacency list
        adj = {}
        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)
        
        # depth-first search
        res = ["JFK"]
        def dfs(v):
            if len(res) == len(tickets) + 1:
                return True
            if not adj[v]:
                return False
            for i, u in enumerate(adj[v]):
                res.append(u)
                adj[v].remove(u)
                if dfs(u):
                    return True
                adj[v].insert(i, u)
                res.pop()
            return False
        
        return res if dfs("JFK") else False

        