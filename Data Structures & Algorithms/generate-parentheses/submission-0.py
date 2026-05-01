class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(countopen, countclose, path):
            if countopen == n and countclose == n:
                res.append(''.join(path))
                return
            
            if countopen < n:
                path.append('(')
                backtrack(countopen + 1, countclose, path)
                path.pop()
            
            if countclose < countopen:
                path.append(')')
                backtrack(countopen, countclose + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res