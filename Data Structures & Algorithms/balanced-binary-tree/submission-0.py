# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def getHeight(root):
            if not root: return 0
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        res = abs(getHeight(root.left) - getHeight(root.right)) <= 1

        return res and self.isBalanced(root.left) and self.isBalanced(root.right)