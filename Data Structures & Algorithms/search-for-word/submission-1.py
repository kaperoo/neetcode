class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        self.visited = [[True]*len(board[0]) for x in range(len(board))]

        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.explore(x,y,0):
                    return True
        return False

    def explore(self, x, y, idx):
        if not self.board[x][y] == self.word[idx]:
            return False
        
        if idx == len(self.word)-1:
            return True

        self.visited[x][y] = False
        if x > 0 and self.visited[x-1][y]:
            if self.explore(x-1,y,idx+1):
                return True
        if y > 0 and self.visited[x][y-1]:
            if self.explore(x,y-1,idx+1):
                return True
        if x < len(self.board)-1 and self.visited[x+1][y]:
            if self.explore(x+1,y,idx+1):
                return True
        if y < len(self.board[0])-1 and self.visited[x][y+1]:
            if self.explore(x,y+1,idx+1):
                return True

        self.visited[x][y] = True
        return False