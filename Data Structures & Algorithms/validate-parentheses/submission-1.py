class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in match.values():         # opening
                stack.append(ch)
            else:                            # closing
                if not stack or stack[-1] != match.get(ch):
                    return False
                stack.pop()

        return not stack
