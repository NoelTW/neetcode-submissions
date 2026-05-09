class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visit = set()
        def bfs(node):
            que = deque([node])
            visit.add(node)
            while que:
                curr = que.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        que.append(neighbor)

        ans = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                ans += 1
        return ans
