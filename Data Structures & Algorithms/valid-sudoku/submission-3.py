class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sub_boxes = defaultdict(set)
        N = len(board)
        for r in range(N):
            for c in range(N):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in sub_boxes[(r//3, c // 3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                sub_boxes[(r//3, c //3)].add(num)
            
        return True