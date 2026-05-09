class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # 1. 統計 t 的字元需求
        need = Counter(t)
        missing = len(t)  # 還需要匹配的字元總數
        
        # 記錄最小視窗的資訊 (長度, 起始點)
        # 初始設為無限大，方便比較
        min_len = float('inf')
        start_index = 0
        
        l = 0
        # 2. 移動右指針 r
        for r, char in enumerate(s):
            # 如果當前字元是我們需要的 (need[char] > 0)，則 missing 減 1
            # 注意：如果 char 不在 t 中，need[char] 預設是 0，這裡判斷 > 0 很關鍵
            if need[char] > 0:
                missing -= 1
            
            # 無論是否需要，都將該字元在 need 中的計數減 1
            # 如果變負數，代表視窗內該字元多餘了
            need[char] -= 1
            
            # 3. 當 missing 為 0 時，代表視窗已包含所有 t 的字元 (Valid Window)
            while missing == 0:
                # 更新最小視窗紀錄
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    start_index = l
                
                # 4. 嘗試收縮左指針 l
                # 我們要移除 s[l]，所以要把他在 need 中的計數加回來
                need[s[l]] += 1
                
                # 如果加回來後大於 0，代表我們移除了一個「原本是必須」的字元
                # 這時視窗變得不合法了，missing 必須 +1，並跳出 while 迴圈繼續移動 r
                if need[s[l]] > 0:
                    missing += 1
                
                l += 1
                
        return s[start_index : start_index + min_len] if min_len != float('inf') else ""