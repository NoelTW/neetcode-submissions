class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter =  [0] * 26
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            counter[ord(char_s) - ord('a')] += 1
            counter[ord(char_t) - ord('a')] -= 1
        for num in counter:
            if num > 0:
                return False
        return True