from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        n = len(digits)

        def backtrack(path, index):
            if index == n:
                res.append("".join(path))
                return

            for ch in hashmap[digits[index]]:
                path.append(ch)
                backtrack(path, index + 1)
                path.pop()

        backtrack([], 0)
        return res