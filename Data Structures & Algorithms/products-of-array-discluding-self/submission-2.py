class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Left pass: product of everything LEFT of i
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
            
        # Right pass: multiply by everything RIGHT of i  
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
            
        return result
