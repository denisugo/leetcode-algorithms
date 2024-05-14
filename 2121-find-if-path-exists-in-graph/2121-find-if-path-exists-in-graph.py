class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        seen = set()
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            for vertex in graph[node]:
                if vertex not in seen:
                    seen.add(vertex)
                    if vertex == destination or dfs(vertex):
                        return True
                
        seen.add(source)
        
        return dfs(source)
        