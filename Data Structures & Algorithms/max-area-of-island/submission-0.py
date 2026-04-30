class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = [[True]*len(grid[0]) for x in range(len(grid))]
        maximum = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if self.visited[x][y]:
                    count = self.recurse(x,y)
                    maximum = max(maximum,count)

        return maximum

    def recurse(self,x,y):
        self.visited[x][y] = False
        
        if self.grid[x][y] == 0:
            return 0

        up,down,left,right = 0,0,0,0


        if x > 0 and self.visited[x-1][y]:
            up = self.recurse(x-1,y)
        if y > 0 and self.visited[x][y-1]:
            left = self.recurse(x,y-1)
        if x < len(self.grid)-1 and self.visited[x+1][y]:
            down = self.recurse(x+1,y)
        if y < len(self.grid[0])-1 and self.visited[x][y+1]:
            right = self.recurse(x,y+1)

        return sum([up,down,left,right,1])