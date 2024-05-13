class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # find indegree of 0
        indegree = [0] * n
        for _, y in edges:
            # y - to
            indegree[y] += 1

        return [node for node in range(n) if indegree[node] == 0]