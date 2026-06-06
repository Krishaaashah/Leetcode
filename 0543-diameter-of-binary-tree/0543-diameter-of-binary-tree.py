# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        self.max_depth = 0
        self.depth = 0
        
        def calculateDepth(node):
            if not node:
                return 0
            
            left_height = calculateDepth(node.left)
            right_height = calculateDepth(node.right)

            depth = left_height + right_height

            self.max_depth = max(self.max_depth,depth)


            return 1+max(left_height, right_height)

        calculateDepth(root)
        return self.max_depth





        


        