class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.res = []

        self.heights = heights
        self.h = len(heights)-1
        self.w = len(heights[0])-1
        self.grid = [[None]*(self.w+1) for x in range(self.h+1)]
        for x in range(self.h+1):
            for y in range(self.w+1):
                if (x in [0,self.h]) or (y in [0,self.w]):
                    p = x==0 or y==0
                    a = x==self.h or y==self.w
                    self.propagate(x,y,[p,a])

        for x in range(self.h+1):
            for y in range(self.w+1):
                if self.grid[x][y] == [True,True]:
                    self.res.append([x,y])

        return self.res
    
    def propagate(self,x,y,t):
        if self.grid[x][y] is None:
            self.grid[x][y] = t.copy()
        else:
            self.grid[x][y][0] = t[0] or self.grid[x][y][0] 
            self.grid[x][y][1] = t[1] or self.grid[x][y][1] 
        val = self.heights[x][y]
        
        if x > 0 and self.heights[x-1][y] >= val:
            if self.grid[x-1][y] not in [t,[True,True]]:
                self.propagate(x-1,y,self.grid[x][y])

        if y > 0 and self.heights[x][y-1] >= val:
            if self.grid[x][y-1] not in [t,[True,True]]:
                self.propagate(x,y-1,self.grid[x][y])

        if x < self.h and self.heights[x+1][y] >= val:
            if self.grid[x+1][y] not in [t,[True,True]]:
                self.propagate(x+1,y,self.grid[x][y])

        if y < self.w and self.heights[x][y+1] >= val:
            if self.grid[x][y+1] not in [t,[True,True]]:
                self.propagate(x,y+1,self.grid[x][y])



    # def search(self,x,y):

        # if self.grid[x][y] is not None:
        #     return
        # p,a = False,False
        # if x==0 or y==0:
        #     p = True
        # if x==self.h or y==self.w:
        #     a = True

        # val = self.heights[x][y]
        # self.grid[x][y] = (p,a)

        # if x > 0 and self.heights[x-1][y] <= val:
        #     if self.grid[x-1][y] is None:
        #         ret = self.search(x-1,y)
        #     else:
        #         ret = self.grid[x-1][y]
        #     p = p or ret[0]
        #     a = a or ret[1]
        # if y > 0 and self.heights[x][y-1] <= val:
        #     if self.grid[x][y-1] is None:
        #         ret = self.search(x,y-1)
        #     else:
        #         ret = self.grid[x][y-1]
        #     p = p or ret[0]
        #     a = a or ret[1]
        # if x < self.h and self.heights[x+1][y] <= val:
        #     if self.grid[x+1][y] is None:
        #         ret = self.search(x+1,y)
        #     else:
        #         ret = self.grid[x+1][y]
        #     p = p or ret[0]
        #     a = a or ret[1]
        # if y < self.w and self.heights[x][y+1] <= val:
        #     if self.grid[x][y+1] is None:
        #         ret = self.search(x,y+1)
        #     else:
        #         ret = self.grid[x][y+1]
        #     p = p or ret[0]
        #     a = a or ret[1]

        
        # if p and a:
        #     self.res.append([x,y])
        # self.grid[x][y] = (p,a) 

        # return (p,a)

        