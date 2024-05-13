class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()        
        def dfs(keys):
            for key in keys:
                if key not in seen:
                    seen.add(key)
                    dfs(rooms[key])
        seen.add(0)
        dfs(rooms[0])
        return len(seen) == len(rooms)
        