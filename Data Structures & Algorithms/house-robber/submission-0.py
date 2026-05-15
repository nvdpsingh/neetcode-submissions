class Solution:
    def rob(self, nums: List[int]) -> int:
        next1 = next2 = 0    # dp[n] = dp[n+1] = 0 (no houses left)
        for i in range(len(nums) - 1, -1, -1):   # start from last index, not n-2
            curr = max(next1, nums[i] + next2)
            next2 = next1
            next1 = curr
        return next1         # dp[0], the answer