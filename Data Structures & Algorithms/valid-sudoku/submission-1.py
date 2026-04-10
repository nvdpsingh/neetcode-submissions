class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for i in range(9):
            dictt = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            for j in range(9):
                if board[i][j]==".":
                    continue
                dictt[board[i][j]]+=1
            for key, val in dictt.items():
                if val>=2:
                    return False
        for i in range(9):
            dictt = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
            for j in range(9):
                if board[j][i]==".":
                    continue
                dictt[board[j][i]]+=1
            for key, val in dictt.items():
                if val>=2:
                    return False
            
        for box_row in range(3):
            for box_col in range(3):
                dictt = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
                for i in range(3):
                    for j in range(3):
                        val = board[box_row*3 + i][box_col*3 + j]
                        if val == ".":
                            continue
                        dictt[val] += 1
                for key, val in dictt.items():
                    if val >= 2:
                        return False
        return True
