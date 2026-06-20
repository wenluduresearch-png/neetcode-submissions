import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.checkDuplicates(board[i]):
                return False

        for col in zip(*board):
            if not self.checkDuplicates(col):
                return False
        arr = np.array(board)
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not self.checkDuplicates(arr[r:r+3, c:c+3].reshape(-1)):
                    return False

        return True


    
    def checkDuplicates(self, checkLs: List[str]) -> bool:
        checkLsNoDots = []
        for s in checkLs:
            if s != '.':
                checkLsNoDots.append(s)
        # print(checkLsNoDots)
        return len(checkLsNoDots) == len(set(checkLsNoDots))
                    