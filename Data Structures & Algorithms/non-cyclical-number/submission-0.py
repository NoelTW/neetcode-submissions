class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while True:
            curr_sum = 0
            while n:
                curr_sum += (n % 10) ** 2
                n //= 10
            
            if curr_sum == 1:
                return True
            if curr_sum in s:
                return False
            
            n = curr_sum
            s.add(curr_sum)