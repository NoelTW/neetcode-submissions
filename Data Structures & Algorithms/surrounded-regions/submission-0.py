class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r, c, visit):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] == "X":
                return
            visit.add((r,c))
            board[r][c] = "T"
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)

        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c, set())
            if board[ROWS -1 ][c] =="O":
                dfs(ROWS- 1, c, set())
        
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0, set())
            if board[r][COLS - 1] =="O":
                dfs(r, COLS - 1, set())
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    continue
        