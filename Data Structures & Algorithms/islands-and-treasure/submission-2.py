class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.inf = 2147483647
        self.grid = grid
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if self.grid[x][y] == 0:
                    self.propagate(x,y,0)
                # if self.grid[x][y] == -1:
                #     continue
                # res = self.search(x,y,set())
                # if res != 2147483647:
                #     self.grid[x][y]=res

    def propagate(self,x,y,i):
        # if self.grid[x][y] == -1:
            # return
        if i > self.grid[x][y]:
            # print(i,self.grif[x][y])
            return

        self.grid[x][y] = i
        
        if x > 0:
            self.propagate(x-1,y,i+1)
        if y > 0:
            self.propagate(x,y-1,i+1)
        if x < len(self.grid)-1:
            self.propagate(x+1,y,i+1)
        if y < len(self.grid[0])-1:
            self.propagate(x,y+1,i+1)
        


    # def search(self,x,y,vis):
    #     visited = vis.copy()
    #     visited.add((x,y))
    #     if self.grid[x][y] == 0:
    #         return 0
    #     elif self.grid[x][y] == -1:
    #         return 2147483647

    #     up,down,left,right = [self.inf]*4

    #     # if x > 0:
    #     if x > 0 and (x-1,y) not in visited:
    #         up = self.search(x-1,y,visited)
    #     # if y > 0:
    #     if y > 0 and (x,y-1) not in visited:
    #         left = self.search(x,y-1,visited)
    #     # if x < len(self.grid)-1:
    #     if x < len(self.grid)-1 and (x+1,y) not in visited:
    #         down = self.search(x+1,y,visited)
    #     # if y < len(self.grid[0])-1:
    #     if y < len(self.grid[0])-1 and (x,y+1) not in visited:
    #         right = self.search(x,y+1,visited)

    #     # self.grid[x][y] = min(min([up,down,left,right])+1,2147483647)
    #     # return self.grid[x][y]
    #     return min(min([up,down,left,right])+1,2147483647)

