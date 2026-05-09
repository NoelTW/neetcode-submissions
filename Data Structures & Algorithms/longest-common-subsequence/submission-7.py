class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        f = [0] * (m + 1)
        
        for x in text1:
            pre = 0 # 每一列開始時，左上角(f[i-1][j-1]) 初始為 0
            for j in range(m):
                tmp = f[j+1] # 1. 先把「上方」的值存起來，它會是下一個 j 的「左上角」
                if x == text2[j]:
                    f[j+1] = pre + 1 # 2. 使用暫存的 pre (左上角)
                else:
                    f[j+1] = max(f[j+1], f[j]) # 3. 取「上方」與「左邊」的最大值
                pre = tmp # 4. 更新 pre，供下一次迴圈使用
        return f[m]