class Solution:
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        for x, y in connections:
            roads.add((x, y))
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        def dfs(city):
            ans = 0
            for destination in graph[city]:
                if destination not in seen:
                    seen.add(destination)
                    if (destination, city) not in roads:
                        ans += 1
                    ans += dfs(destination)
            return ans

        seen.add(0)
        return dfs(0)
            