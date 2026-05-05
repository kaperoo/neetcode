class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.h = len(board)
        self.w = len(board[0])
        self.board = board
        self.grid = [['X']*(self.w) for x in range(self.h)]

        for x in range(self.h):
            for y in range(self.w):
                if x in [0,self.h-1] or y in [0,self.w-1]:
                    self.propagate(x,y)
        for x in range(self.h):
            for y in range(self.w):       
                self.board[x][y] = self.grid[x][y]
        


    def propagate(self,x,y):
        if self.grid[x][y] == 'O' or self.board[x][y] == 'X':
            return

        self.grid[x][y] = 'O'

        if x>0:
            self.propagate(x-1,y)
        if y>0:
            self.propagate(x,y-1)
        if x<self.h-1:
            self.propagate(x+1,y)
        if y<self.w-1:
            self.propagate(x,y+1)
