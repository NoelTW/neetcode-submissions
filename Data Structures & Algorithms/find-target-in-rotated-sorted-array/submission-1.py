
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # 判斷左半部分 [left...mid] 是否有序
            if nums[left] <= nums[mid]: # 左半部分有序
                # 檢查 target 是否在左半部分
                if nums[left] <= target < nums[mid]:
                    # target 在左半部分有序區間內，縮小右邊界
                    right = mid - 1
                else:
                    # target 不在左半部分，說明 target 在右半部分 (可能有序可能無序)
                    left = mid + 1
            # 否則，右半部分 [mid...right] 有序
            else: # nums[left] > nums[mid], 意味著右半部分有序
                # 檢查 target 是否在右半部分
                if nums[mid] < target <= nums[right]:
                    # target 在右半部分有序區間內，縮小左邊界
                    left = mid + 1
                else:
                    # target 不在右半部分，說明 target 在左半部分 (可能有序可能無序)
                    right = mid - 1
        
        # 迴圈結束，如果還沒找到，表示 target 不存在
        return -1