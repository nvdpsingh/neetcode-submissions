class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = ""
        right = ""

        clean = ''.join(c for c in s if c.isalnum()).lower()
        for i in range((len(clean)//2)):
            left=clean[i]
            right=clean[len(clean)-1-i]
            if left!=right:
                return False

        return True