class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. parse edges into hashmap
        # 2. create dfs algorithm
        # 3. iterate over all nodes and calculate connected components
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        ans = 0
        for node in range(n):
            if node not in seen:
                seen.add(node)
                ans += 1
                dfs(node)
                
        return ans