from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        seen = set()
        l = len(isConnected)
        graph = defaultdict(list)

        for i in range(l):
            for j in range(i + 1, l):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        def travers(ver):
            if ver in seen:
                return
            seen.add(ver)
            for conn in graph[ver]:
                travers(conn)

        for ver in range(l):
            if(not ver in seen):
                ans += 1
                travers(ver)

        return ans
        