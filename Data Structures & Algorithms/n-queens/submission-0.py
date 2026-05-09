class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        board  = [["." for _ in range(n)] for _ in range(n)]
        print(board)

        def is_valid(board, row, col):
            # Check up 
            for r in range(row):
                if board[r][col] == "Q":
                    return False
            # check left up 
            r, c = row - 1, col - 1
            while r >= 0 and c >=0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # check left up
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            return True

        def backtrack(row, board):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = "Q"
                    backtrack(row+1, board)
                    board[row][col] = "."

        backtrack(0, board)
        return res
