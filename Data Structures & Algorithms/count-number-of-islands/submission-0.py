class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])

        def exploreLand(i, j):
            if i > 0 and grid[i-1][j] == "1":
                grid[i-1][j] = "0"
                exploreLand(i-1,j)
            if j > 0 and grid[i][j-1] == "1":
                grid[i][j-1] = "0"
                exploreLand(i,j-1)
            if i < m-1 and grid[i+1][j] == "1":
                grid[i+1][j] = "0"
                exploreLand(i+1,j)
            if j < n-1 and grid[i][j+1] == "1":
                grid[i][j+1] = "0"
                exploreLand(i,j+1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    exploreLand(i,j)
        return count
        

    