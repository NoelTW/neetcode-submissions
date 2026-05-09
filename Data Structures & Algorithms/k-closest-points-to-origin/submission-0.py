class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [ ( - (x**2 + y**2)**0.5 , x, y) for x, y in points ]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        print(heap)
        
        min_distance = float('inf')
        res = []
        while heap:
            distance, x, y = heapq.heappop(heap)
            if distance > min_distance:
                break
            res.append([x,y])
        return res