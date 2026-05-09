class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = [ (- ((x**2 + y**2) ** 0.5) , [x, y]) for x, y in points]
        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        return [res for _, res in max_heap]