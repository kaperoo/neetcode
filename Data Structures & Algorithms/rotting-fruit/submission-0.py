class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.time = [[0]*len(grid[0]) for x in range(len(grid))]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    self.time[x][y] = -1 if not self.time[x][y] else self.time[x][y]
                elif grid[x][y] == 2:
                    self.propagate(x,y,0)

        maximum = 0
        for o in self.time:
            maximum = max(maximum,max(o))
            if min(o) == -1:
                return -1
        return maximum            


    def propagate(self,x,y,i):
        if (i > self.time[x][y] and self.time[x][y] > 0):
            return
        self.time[x][y] = i

        if x > 0 and self.grid[x-1][y] == 1:
            self.propagate(x-1,y,i+1)
        if y > 0 and self.grid[x][y-1] == 1:
            self.propagate(x,y-1,i+1)
        if x < len(self.grid)-1 and self.grid[x+1][y] == 1:
            self.propagate(x+1,y,i+1)
        if y < len(self.grid[0])-1 and self.grid[x][y+1] == 1:
            self.propagate(x,y+1,i+1)

        
        