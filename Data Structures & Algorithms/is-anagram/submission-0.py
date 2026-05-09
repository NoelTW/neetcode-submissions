class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        right = {}
        left = {}

        for s_char in s:
            right[s_char] = right.get(s_char, 0) + 1
        
        for t_char in t:
            left[t_char] = left.get(t_char,0) + 1
        

        return right == left