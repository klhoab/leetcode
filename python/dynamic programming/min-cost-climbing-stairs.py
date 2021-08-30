#https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache(None)
        def findCostAtFloor(n) -> int:
            if n == 2:
                return min(cost[0], cost[1])
            if n <= 1:
                return 0
            return min(cost[n-1] + findCostAtFloor(n-1), cost[n-2] + findCostAtFloor(n-2))
        
        return findCostAtFloor(len(cost))
            