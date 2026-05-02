class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        # Count characters in s
        for ch in s:
            if ch in count_s:
                count_s[ch] += 1
            else:
                count_s[ch] = 1

        # Count characters in t
        for ch in t:
            if ch in count_t:
                count_t[ch] += 1
            else:
                count_t[ch] = 1

        # Two strings are anagrams if their counts are equal
        return count_s == count_t
