# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, min_so_far, max_so_far):
            curr_min = min_so_far
            curr_max = max_so_far

            if root == None:
                return 0

            if root.val < curr_min:
                curr_min = root.val
            if root.val > curr_max:
                curr_max = root.val

            l = dfs(root.left, curr_min, curr_max)
            r = dfs(root.right, curr_min, curr_max)

            return max(curr_max-curr_min, l, r)

        return dfs(root, 10**5, 0)