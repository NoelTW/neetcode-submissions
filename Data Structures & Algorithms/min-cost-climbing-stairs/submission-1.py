class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        if len(cost) < 2:
            return 0
        first_step = cost[0]
        second_step = cost[1]
        for i in range(2,len(cost)):
            temp_step = min(first_step, second_step) + cost[i]
            first_step = second_step
            second_step = temp_step

        
        return min(first_step, second_step)