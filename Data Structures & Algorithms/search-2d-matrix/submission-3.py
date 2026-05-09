class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        H, W  = len(matrix), len(matrix[0])

        l, r = 0, H * W - 1
    
        while l <= r:
            m = l + ( r - l) // 2
            h, w = m // W, m % W
            if matrix[h][w] > target:
                r = m - 1
            elif matrix[h][w] < target:
                l = m + 1
            else:
                return True
        
        return False
        