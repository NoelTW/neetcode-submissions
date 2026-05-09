class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(m):
            t = 0
            for pile in piles:
                t += math.ceil(pile / m)
            return t <= h
        l, r = 1, max(piles) + 1
        while l < r:
            m = (l + r) // 2
            if ok(m):
                r = m 
            else:
                l = m +1
        return l

