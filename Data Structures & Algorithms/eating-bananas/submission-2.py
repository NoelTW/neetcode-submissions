class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def get_eat_time(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
            return time


        
        r = max(piles)
        l = 1

        while l <= r:
            m = ( l + r) // 2
            print(m,get_eat_time(m))
            if get_eat_time(m) > h:
                l = m + 1
            elif get_eat_time(m) <= h:
                r = m - 1
            # else:
            #     break
        
        return l