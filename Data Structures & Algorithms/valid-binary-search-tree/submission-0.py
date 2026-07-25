# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
# Every node must be within a valid range.
# Initially the range is (-∞, +∞).
# When going left, update the maximum value.
# When going right, update the minimum value.
# If any node is outside its range, return False.
# Otherwise return True.
        def dfs(node, minimum, maximum):
            if not node:
                return True
            if not minimum < node.val < maximum:
                return False
            return (dfs(node.left, minimum, node.val) and
                    dfs(node.right, node.val, maximum))
        
        return dfs(root, float("-inf"), float("inf"))

        