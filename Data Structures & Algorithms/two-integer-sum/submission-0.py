class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        
        for i in range(n):
            search = target - nums[i]
            if search in nums:
                for j in range(i+1,n):
                    if search == nums[j]:
                        return [i,j]
        