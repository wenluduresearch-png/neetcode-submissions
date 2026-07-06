# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root and subRoot: return False

        def isSame(t1, t2):
            if not t1 and not t2: return True
            if (not t1 and t2) or (not t2 and t1): return False
            return t1.val == t2.val and isSame(t1.left, t2.left) and isSame(t1.right, t2.right)
        
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)