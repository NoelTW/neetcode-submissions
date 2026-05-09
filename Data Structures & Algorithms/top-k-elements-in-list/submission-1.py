from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)

        for num in nums:
            table[num] += 1   
        ans = []
        for key, val in sorted(table.items(), key=lambda item: item[1])[-k:]:
            ans.append(key)
        return ans