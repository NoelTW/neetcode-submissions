class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_board = [0] * (ord("z") - ord("A") + 1)
        for c in t:
            t_board[ord(c) - ord("A")] += 1
        
        min_len = float('inf')
        res_range = (-1, -1)
        l = 0
        for r in range(len(s)):
            t_board[ord(s[r]) - ord("A")] -= 1
            while l <= r and all(i <= 0 for i in t_board):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res_range = (l, r)
                t_board[ord(s[l]) - ord("A")] += 1
                l += 1

        return s[res_range[0] : res_range[1] + 1] if res_range[0] >= 0 else ""