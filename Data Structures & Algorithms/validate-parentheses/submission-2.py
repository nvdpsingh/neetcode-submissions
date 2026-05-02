class Solution:
    def isValid(self, s: str) -> bool:
        samp = []

        for i in range(len(s)):
            if s[i] == ']':
                if not samp or samp[-1] != '[':
                    return False
                samp.pop()

            elif s[i] == ')':
                if not samp or samp[-1] != '(':
                    return False
                samp.pop()

            elif s[i] == '}':
                if not samp or samp[-1] != '{':
                    return False
                samp.pop()

            else:
                samp.append(s[i])

        return len(samp) == 0