class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)
        max_length = 1
        
        for num in nums:  
            if num - 1 not in num_set:  
                curr = num
                length = 1
                while curr + 1 in num_set:
                    curr += 1
                    length += 1
                max_length = max(max_length, length)
        
        return max_length
