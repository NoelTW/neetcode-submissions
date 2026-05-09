class Solution:
    def reverse(self, x: int) -> int:
        ans, temp = 0, abs(x)
        
        while temp:
            ans = ans * 10 + temp % 10
            temp //= 10
        
        if x < 0: ans = -ans
        
        return ans if -(2**31) <= ans <= 2**31 - 1 else 0