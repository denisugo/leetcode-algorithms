# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root == None: 
                return 0;
        
            l = dfs(root.left)
            r = dfs(root.right)
        
            self.ans = max(l + r, self.ans)
        
            return max(l, r) + 1
        
        dfs(root)
        return self.ans     