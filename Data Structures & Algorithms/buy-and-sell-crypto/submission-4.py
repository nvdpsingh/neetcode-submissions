class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxp = 0
        for right in range(1,len(prices)):
            if prices[right]-prices[left]<0:
                left=right
            else:
                profit = prices[right]-prices[left]
                maxp = max(maxp,profit)
        return maxp