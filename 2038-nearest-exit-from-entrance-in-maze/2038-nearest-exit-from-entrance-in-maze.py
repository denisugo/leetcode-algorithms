class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(maze)
        n = len(maze[0])

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m and maze[y][x] == "."

        def is_exit(x, y):
            return x == 0 or x == n - 1 or y == 0 or y == m - 1
        entry_point = (entrance[1], entrance[0])
        visited = {entry_point}
        q = deque([entry_point])
        steps = 0
        
        while q: 
            for _ in range(len(q)):
                x, y = q.pop()
                if not (x, y) == entry_point and is_exit(x, y):
                    return steps
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if (new_x, new_y) not in visited and is_valid(new_x, new_y):
                        q.appendleft((new_x, new_y))
                        visited.add((new_x, new_y))
            steps += 1
        return -1
        