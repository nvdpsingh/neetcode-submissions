class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacknum = []
        res = None
        for i in tokens:
            if i in ('+', '-', '*', '/'):
                num1 = stacknum.pop()
                num2 = stacknum.pop()
                if i =='+':
                    res = num2+num1
                    stacknum.append(res)
                elif i =='-':
                    res = num2-num1
                    stacknum.append(res)
                elif i =='*':
                    res = num2*num1
                    stacknum.append(res)
                else:
                    res = int(num2/num1)
                    stacknum.append(res)
            else:
                stacknum.append(int(i))
        return stacknum[0]
