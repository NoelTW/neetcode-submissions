class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)

        max_heap = [-cnt for cnt in counter.values()]
        
        heapq.heapify(max_heap)

        time = 0
        
        que = deque()

        while max_heap or que:
            time += 1
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    que.append([count, time + n])
            if que and que[0][1] == time:
                heapq.heappush(max_heap, que.popleft()[0])
        
        return time