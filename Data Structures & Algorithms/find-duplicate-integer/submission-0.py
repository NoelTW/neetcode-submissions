class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # naive
        table = defaultdict(int)
        for num in nums:
            table[num] += 1
        
        for key in table:
            if table[key] > 1:
                return key
                