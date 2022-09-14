# 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        min_cost = [0] * n
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        for i in range(2, n):
            min_cost[i] = cost[i] + min(min_cost[i - 1], min_cost[i - 2])
        return min(min_cost[n - 1], min_cost[n - 2])
