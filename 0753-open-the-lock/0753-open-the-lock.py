class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        seen = set(deadends)
        changes = [1, -1]
        def get_next(num, change):
           return (num + change) % 10

        queue = deque(["0000"])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()
                if node == target:
                    return steps
                for i in range(4):
                    for change in changes:
                        new_node = node[:i] + str(get_next(int(node[i]), change)) + node[i + 1:]
                        if new_node not in seen:
                            seen.add(new_node)
                            queue.appendleft(new_node)
            steps += 1
        
        return -1