class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finallist = []
        nums = sorted(nums)
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                l,r = i+1, len(nums)-1
                while l<r:
                    if nums[l]+nums[r]== (0-nums[i]):
                        finallist.append([nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[l]+nums[r]> (0-nums[i]):
                        r-=1
                    elif nums[l]+nums[r]< (0-nums[i]):
                        l+=1
                seen.add(nums[i])
            else:
                pass
        return finallist