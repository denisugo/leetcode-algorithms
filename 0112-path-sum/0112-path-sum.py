# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            
            curr += node.val

            if node.left == None and node.right == None:  # leaf
                return curr == targetSum

            left = dfs(node.left, curr)
            if left:
                return left
            right = dfs(node.right, curr)
            if right:
                return right

            return False

        return dfs(root, 0)
