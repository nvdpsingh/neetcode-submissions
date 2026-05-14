class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(n-1,-1,-1):
            one = dp[i+1]
            two = dp[i+2] if i+2<=n else 0
            dp[i] = cost[i]+ min(one,two)

        return min(dp[0],dp[1])
            
            

