class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = [[]]

        for num in nums:
            new_subsets = []
            for subset in final:
                new_subsets.append(subset + [num])
            final.extend(new_subsets)

        return final