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
            for dest in graph[ver]:
                if dest not in seen:
                    seen.add(dest)
                    travers(dest)

        for ver in range(l):
            if ver not in seen:
                seen.add(ver)
                travers(ver)
                ans += 1

        return ans
        