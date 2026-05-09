class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                curr_len = 1
                while num + 1 in nums_set:
                    curr_len += 1
                    num += 1
                res = max(res, curr_len)
        
        return res
