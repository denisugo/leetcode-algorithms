class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        ans = 0
        while len(sticks) > 1:
            price = heapq.heappop(sticks) + heapq.heappop(sticks)
            ans += price
            heapq.heappush(sticks, price)
        
        return ans