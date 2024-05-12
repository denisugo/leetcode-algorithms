class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        ans = 0
        x_len = len(grid)
        y_len = len(grid[0])
        def is_valid(row, col): 
            return 0 <= row < x_len and 0 <= col < y_len and grid[row][col] == "1"
            
        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        for i in range(x_len):
            for j in range(y_len):
                if (i, j) not in seen and grid[i][j] == "1":
                    seen.add((i, j))
                    dfs(i, j)
                    ans += 1

        return ans
        