class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0])
        
        zeros = []
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zeros.append((r, c))

        def helper(r , c):
            for i in range(n):
                matrix[r][i] = 0
            for i in range(m):
                matrix[i][c] = 0

        while zeros:
            r , c = zeros.pop()
            helper(r,c)
        
    