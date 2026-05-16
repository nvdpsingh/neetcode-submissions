class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(nums):
            next1 = next2 = 0
            for n in nums:
                new = max(n+next1,next2)
                next1 = next2
                next2 = new
            return next2
        return max(nums[0],helper(nums[:-1]),helper(nums[1:]))
        
        