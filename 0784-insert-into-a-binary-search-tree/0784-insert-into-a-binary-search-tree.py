# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root: 
            return TreeNode(val)
            
            
        def insert(root):
            v = root.val
            
            if v > val:
                if root.left:
                    return insert(root.left)
                else:
                    root.left = TreeNode(val)
                    return
            else:
                if root.right:
                    return insert(root.right)
                else:
                    root.right = TreeNode(val)
                    return
                
        insert(root)
        return root