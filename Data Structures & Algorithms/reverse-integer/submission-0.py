class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10  + x % 10
            x //= 10
        
        if neg:
            ans = -ans
        
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        return ans