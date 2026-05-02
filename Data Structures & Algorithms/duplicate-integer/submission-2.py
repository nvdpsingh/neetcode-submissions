class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for items in nums:
            if items in seen:
                return True
            else:
                seen.add(items)
        return False