from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        seen = set()
        l = len(isConnected)
        graph = defaultdict(list)

        for i in range(l):
            for j in range(l):
                if isConnected[i][j]:
                    graph[i].append(j)

        def travers(ver):
            if ver in seen:
                return
            seen.add(ver)
            conns = graph[ver]
            for conn in conns:
                travers(conn)

        for key in graph.keys():
            if(not key in seen):
                ans += 1
                travers(key)

        return ans
        