class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        next1=next2=0
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i] = min(cost[i]+next1,cost[i]+next2)
            next1= dp[i]
            next2 = dp[i+1]
        return min(dp[0],dp[1])
            

