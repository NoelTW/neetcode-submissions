class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst) 


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph:
            # has source
            if dst in self.graph[src]:
                self.graph[src].remove(dst)
                return True
            else:
                return False
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        # BFS
        if src not in self.graph:
            return False

        visit = set()
        visit.add(src)
        que = deque()
        que.append(src)
        while que:
            for _ in range(len(que)):
                curr = que.popleft()
                print(curr)
                if curr ==  dst:
                    return True
                for neighbor in self.graph[curr]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        que.append(neighbor)
        
        return False
                


