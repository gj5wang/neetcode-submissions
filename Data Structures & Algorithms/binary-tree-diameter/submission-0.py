# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #track the longest of the diameter of self.left and self.right + 1
        if not root:
            return 0

        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max (self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))#the case where the max diameter dont pass through the node
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

