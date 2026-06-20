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
        if not self.checkDuplicates(arr[0:3, 0:3].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[0:3, 3:6].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[0:3, 6:9].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[3:6, 3:6].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[3:6, 0:3].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[3:6, 6:9].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[6:9, 3:6].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[6:9, 0:3].reshape(-1)):
            return False
        if not self.checkDuplicates(arr[6:9, 6:9].reshape(-1)):
            return False

        return True


    
    def checkDuplicates(self, checkLs: List[str]) -> bool:
        checkLsNoDots = []
        for s in checkLs:
            if s != '.':
                checkLsNoDots.append(s)
        # print(checkLsNoDots)
        return len(checkLsNoDots) == len(set(checkLsNoDots))
                    