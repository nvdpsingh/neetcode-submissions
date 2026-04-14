class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictt = {}
        for c in nums:
            if c in dictt:
                dictt[c]+=1
            else:
                dictt[c]=1
            
        return max(dictt, key = dictt.get)