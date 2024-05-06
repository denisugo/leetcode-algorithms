# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: 
            return 0
        
        v = root.val
        ans = 0
        if not v > high and not v < low:
            ans += v
            ans += self.rangeSumBST(root.left, low, high)
            ans += self.rangeSumBST(root.right, low, high)
        
        if v > high:
            ans += self.rangeSumBST(root.left, low, high)
        if v < low:
            ans += self.rangeSumBST(root.right, low, high)

        return ans
        