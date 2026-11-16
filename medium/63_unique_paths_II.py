class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [1] + [0] * (cols - 1)

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0

                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]

        return dp[cols-1]
