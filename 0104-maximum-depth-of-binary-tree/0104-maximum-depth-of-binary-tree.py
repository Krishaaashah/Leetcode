# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0

        def CalDepth(node):
            if not node:
                return 0
            ld = CalDepth(node.left)
            rd = CalDepth(node.right)


            return max(ld,rd)+1

        return CalDepth(root)


        