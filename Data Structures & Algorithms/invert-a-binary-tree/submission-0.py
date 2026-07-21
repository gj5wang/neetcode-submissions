# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optionanl[TreeNode]) -> Optional[TreeNode]:
        #if empty list the output will be empty
        #if not empty root.left = root.right and vice versa

        if root is None:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.right = left
        root.left = right

        return root