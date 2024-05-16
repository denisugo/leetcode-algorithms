class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        len_x = len(grid)
        len_y = len(grid[0])
        
        def is_valid(row, col):
            return 0 <= row < len_x and 0 <= col < len_y
        
        seen = set()

        def dfs(row, col):
            curr = 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen and grid[new_row][new_col] == 1:
                    seen.add((new_row, new_col))
                    curr += dfs(new_row, new_col)
            return curr
        
        ans = 0
        for row in range(len_x):
            for col in range(len_y):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    ans = max(ans, dfs(row, col))
                    
        return ans
                