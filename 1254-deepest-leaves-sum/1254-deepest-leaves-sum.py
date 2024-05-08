# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        
        queue = deque([root])
        ans = 0
        
        while queue:
            all_leaves = True
            curr = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                curr += node.val
                if node.left or node.right:
                    all_leaves = False
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
            if all_leaves:
                ans = curr
                
        return ans
                
                    
        