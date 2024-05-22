class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 1
        graph = defaultdict(list)
        n = len(bombs)
        
        def is_in_range(x1, y1, x2, y2, r):
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            return r**2 >= (dx**2 + dy**2)
        
        for i in range(n):
            for j in range(n):
                x1, y1, r = bombs[i]
                x2, y2, _ = bombs[j]
                if not i == j and is_in_range(x1, y1, x2, y2, r):
                    graph[i].append(j)
                    
        def dfs(node, seen):
            ans = 1
            for bomb in graph[node]:
                if bomb not in seen:
                    seen.add(bomb)
                    ans += dfs(bomb, seen)
            return ans 
        
        for i in range(n):
            if graph[i]:
                ans = max(ans, dfs(i, {i}))
                
        return ans
                    
            
        