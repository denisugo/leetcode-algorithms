class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        def dfs(idx):
            if not 0 <= idx < len(arr) or idx in seen:
                return False
            
            seen.add(idx)
            
            if arr[idx] == 0:
                return True
            
            greater_idx, less_idx = arr[idx] + idx, idx - arr[idx]
            
            return dfs(greater_idx) or dfs(less_idx)
        
        return dfs(start)
        