class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path,start)->None:
            if sum(path) == target:
                res.append(path[:])
            if sum(path)>target:
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(path,i)
                path.pop()
        backtrack([],0)
        return res