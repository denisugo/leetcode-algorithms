class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restriction = set()
        for node in restricted:
            restriction.add(node)
            
        graph = defaultdict(list)
        for x, y in edges:
            if x not in restriction and y not in restriction:
                graph[x].append(y)
                graph[y].append(x)
            
        seen = {0}
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        
        dfs(0)
            
        return len(seen)
            
            
        