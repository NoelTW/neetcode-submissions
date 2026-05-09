class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(speed, h):
            eh = 0
            for pile in piles:
                eh += math.ceil(pile / speed)
            return eh <= h
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            if can_finish(m, h):
                r = m - 1
            else:
                l = m + 1
        return l