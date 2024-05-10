# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        from_left_to_right = True
        
        while queue:
            length = len(queue)
            
            curr = [0] * length
            for i in range(length):
                node = queue.popleft()
                if(from_left_to_right):
                    curr[i] = node.val
                else:
                    curr[length - i - 1] = node.val
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            ans.append(curr)
            from_left_to_right = not from_left_to_right
        return ans