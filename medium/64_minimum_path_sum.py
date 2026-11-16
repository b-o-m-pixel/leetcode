class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                    
                elif i == 0:
                    dp[j] = grid[i][j] + dp[j-1]
                
                elif j == 0:
                    dp[j] = grid[i][j] + dp[j]
                
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
                
        return dp[cols-1]
