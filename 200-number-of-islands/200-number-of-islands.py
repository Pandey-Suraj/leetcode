class Solution:
    
# here we had done this problem with the use of dfs first we check whether the current index is having 1 or not. if we have 1 in the current row and column then we will call the dfs function and in the dfs function we will find top,bottom,left,right if we find another one from that we will again call the dfs function.

    def dfs(self,grid,r,c):
        grid[r][c] = '0'
        lst = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
        for row, col in lst:
            if row>= 0 and col>=0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == '1':
                self.dfs(grid,row,col)
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]== '1':
                    self.dfs(grid,r,c)
                    island += 1
        
        return island
        