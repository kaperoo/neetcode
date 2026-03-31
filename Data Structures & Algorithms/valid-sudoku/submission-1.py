class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.checkRow(row):
                return False

        if not self.checkCol(board):
            return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.checkBox(i,j,board):
                    return False

        return True

    def checkRow(self, row):
        nums = set()
        for n in row:
            if n == '.':
                continue
            if n in nums:
                return False
            nums.add(n)
        return True

    def checkCol(self, board):
        for i in range(9):
            nums = set()
            for j in range(9):
                n = board[j][i] 
                if n == '.':
                    continue
                elif n in nums:
                    return False
                nums.add(n)
        return True

    def checkBox(self, x,y, board):
        nums = set()
        for i in range(x,x+3):
            for j in range(y,y+3):
                n = board[i][j]
                if n == '.':
                    continue
                if n in nums:
                    return False
                nums.add(n)
        return True