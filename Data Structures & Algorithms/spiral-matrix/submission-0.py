class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l , r = 0, len(matrix[0]) -1 
        t , b = 0, len(matrix) - 1
        count = len(matrix[0]) * len(matrix)
        while (l <= r or b >= t) and count:        
            # l to r
            for i in range(l, r+ 1):
                res.append(matrix[t][i])
                count -= 1
            t += 1
            # t to b
            for i in range(t, b + 1):
                res.append(matrix[i][r])
                count -= 1
            r -= 1
            if count == 0:
                break
            # r to l
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
                count -= 1
            b -= 1
            print(count)
            # b to t
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
                count -= 1
            l += 1

        return res