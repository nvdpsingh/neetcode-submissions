class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        sol = []

        def backtrack(i, path_sum):
            if path_sum == target:
                res.append(sol[:])
                return
            if path_sum > target or i == n:
                return

            # include current
            sol.append(candidates[i])
            backtrack(i + 1, path_sum + candidates[i])
            sol.pop()

            # exclude current, but skip all duplicates of candidates[i]
            j = i + 1
            while j < n and candidates[j] == candidates[i]:
                j += 1
            backtrack(j, path_sum)

        backtrack(0, 0)
        return res