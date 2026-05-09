class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        # find row
        u, b = 0, R - 1
        while u <= b:
            m = u + (b - u) // 2
            lb, ub = matrix[m][0], matrix[m][-1] 
            if lb > target:
                b = m - 1
            elif ub < target:
                u = m + 1
            else:
                break
        row = m
        l, r = 0, C 
        while l < r:
            m = l + (r - l ) // 2
            if matrix[row][m] >= target:
                r = m
            else:
                l = m + 1
        col = l
        if l == C or matrix[row][col] != target:
            return False
        return True
        



            