class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if abs(first) - abs(second) != 0:
                heapq.heappush(stones, first - second)

        return -stones[0] if stones else 0
        
        