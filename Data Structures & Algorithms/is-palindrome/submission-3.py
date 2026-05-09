class Solution:
    def isPalindrome(self, s: str) -> bool:
        ascii = [ord('0') + i for i in range(10)] + [ord('a') + i for i in range(26)]
        l ,r = 0, len(s) - 1 
        s = s.lower()
        while l <= r:
            if ord(s[l]) not in ascii:
                l += 1
                continue  
            if ord(s[r]) not in ascii:
                r -= 1
                continue
            print(s[l], s[r])
            if s[l] == s[r]:
                r -= 1
                l += 1
            else:
                return False
            
        return True

        