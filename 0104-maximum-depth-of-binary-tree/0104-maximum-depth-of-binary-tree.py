# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.depth = 0

        def caldepth(node):
            if not node:
                return 0

            ld = caldepth(node.left)
            rd = caldepth(node.right)

            return max(ld,rd)+1

        return caldepth(root)
        