class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n*n
        graph = [None] * (target + 1)

        reversed = False
        idx = 1
        for y in range(n):
            for x in range(n):
                graph[idx] = board[n - 1 - y][x if not reversed else n - 1 - x]
                idx += 1
            reversed = not reversed
        dist = [-1] * (target + 1)
        dist[1] = 0
        queue = deque([1])

        while queue:
            node = queue.pop()
            for next in range(node + 1, min(node + 6, target) + 1):
                neighbour = next if graph[next] == -1 else graph[next]
                if dist[neighbour] == -1:
                    dist[neighbour] = dist[node] + 1
                    queue.appendleft(neighbour)

        return dist[target]
