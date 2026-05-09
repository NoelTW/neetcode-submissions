class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for array in matrix:
            if target > array[-1]:
                continue
            l, r = 0, len(array) - 1
            while l <= r:
                m = (l+r)// 2
                if target < array[m]:
                    r = m - 1
                elif target > array[m]:
                    l = m + 1
                else:
                    return True   
        return False