# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, low, high):
            if not root:
               return True
            v = root.val
            if not (low < v < high):
                return False
            l = check(root.left, low, v)
            r = check(root.right, v, high)
            return l and r


        return check(root, float("-inf"), float("inf"))
        