# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 2 * (10**9)

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if not root:
            return
        curr_diff = abs(target - root.val)
        old_diff = abs(target - self.ans)
        if curr_diff < old_diff or (curr_diff == old_diff and root.val < self.ans):
            self.ans = root.val

        self.closestValue(root.left, target)
        self.closestValue(root.right, target)

        return self.ans
