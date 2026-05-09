class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            seen.add((r, c))
            for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr == n or nc == m or (nr, nc) in seen:
                    continue
                if dfs(nr, nc, i + 1):
                    return True
            seen.remove((r, c))
            return False
        seen = set()
        n, m = len(board), len(board[0])
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False