# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def getMaxDepth(root):
            if not root: return 0
            if not root.left and not root.right: return 0

            return 1 + max(getMaxDepth(root.left), getMaxDepth(root.right))
        
        res = 0
        left_diameter = getMaxDepth(root.left)
        right_diameter = getMaxDepth(root.right)
        if root.left and root.right: res = left_diameter + right_diameter  + 2
        elif root.left: res = left_diameter + 1
        elif root.right: res = right_diameter + 1
        return max(max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)), 
        res)