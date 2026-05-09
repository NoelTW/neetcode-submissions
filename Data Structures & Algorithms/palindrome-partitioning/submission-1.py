class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        path = []
        ans = []
        def backtrack(l):
            if l == n:
                ans.append(path[:])
                return 
            r = l
            while r < n:
                if ok(l, r):
                    path.append(s[l: r+ 1])
                    backtrack(r + 1)
                    path.pop()
                r += 1
                
        def ok(l, r): # internal interval [l, r]
            while l <= r:
                if s[r] != s[l]:
                    return False
                l += 1
                r -= 1
            return True

        backtrack(0)
        return ans
                
