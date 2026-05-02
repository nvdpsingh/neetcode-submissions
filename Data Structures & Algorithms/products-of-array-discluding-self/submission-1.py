class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finallist=[]
        for i in range(len(nums)):
            left = 0
            right=0
            prodct=0
            if i==0:
                prodct= math.prod(nums[1:len(nums)])
            elif(i==(len(nums)-1)):
                prodct= math.prod(nums[0:(len(nums)-1)])
        
            else:
                left = math.prod(nums[0:i])
                right = math.prod(nums[i+1:len(nums)])
                prodct = left*right
            finallist.append(prodct)
        return finallist
                