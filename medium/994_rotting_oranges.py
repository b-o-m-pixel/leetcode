class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        count_fresh_oranges = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    
                if grid[i][j] == 1:
                    count_fresh_oranges += 1
                    
        minutes = 0
        
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        
        while queue and count_fresh_oranges > 0:
            size = len(queue)
            
            for _ in range(size):
                row, col = queue.popleft()
                
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    
                    if not 0 <= new_row < rows or not 0 <= new_col < cols:
                        continue
                        
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        count_fresh_oranges -= 1
                        queue.append((new_row, new_col))
                    
            minutes += 1
                
        return minutes if count_fresh_oranges == 0 else -1
