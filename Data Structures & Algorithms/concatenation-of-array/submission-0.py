class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        j=0
        while(j<(2*n)):
            for i in range(n):
                ans.append(nums[i])
            j+=n
        return ans
