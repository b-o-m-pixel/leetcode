class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, row, col):
            rows = len(grid)
            cols = len(grid[0])

            if not 0 <= row < rows or not 0 <= col < cols or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                dfs(grid, new_row, new_col)
                

        island_counter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island_counter += 1
                    dfs(grid, i, j)
                                   
        return island_counter        
