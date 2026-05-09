class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}
        for i,num in enumerate( nums ):
            diff = target - num
            if diff in table:
                return [ table[diff], i]
            table[num] = i