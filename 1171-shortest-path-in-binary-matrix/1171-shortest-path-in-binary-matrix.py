from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque([(0, 0)])
        directions = [
            (0, 1),
            (1, 0),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (0, -1),
            (-1, 0),
        ]
        n = len(grid)
        steps = 0
        seen = {(0, 0)}

        def is_valid(row, col):
            return 0 <= col < n and 0 <= row < n and grid[curr_x][curr_y] == 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                row, col = queue.pop()

                if (row, col) == (n - 1, n - 1):
                    return steps

                for dx, dy in directions:
                    curr_x, curr_y = row + dx, col + dy

                    if is_valid(curr_x, curr_y) and (curr_x, curr_y) not in seen:
                        seen.add((curr_x, curr_y))
                        queue.appendleft((curr_x, curr_y))
        return -1