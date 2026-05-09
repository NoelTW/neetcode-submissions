import math
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(cost) != len(gas):
            return -1
        n = len(cost)
        curr_sum = 0
        ans = 0
        total_sum = 0
        for i in range(n):
            curr_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if curr_sum < 0:
                curr_sum = 0 
                ans = i + 1
        if total_sum < 0:
            return -1
        return ans