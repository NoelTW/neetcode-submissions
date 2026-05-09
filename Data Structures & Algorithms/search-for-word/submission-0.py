class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in visit
            ):
                return False
            visit.add((r, c))
            directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
            is_words=[]
            for dr, dc in directions:
                is_words.append( dfs(r + dr, c + dc, i + 1) )
            visit.remove((r,c))
            return any(is_words)
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False