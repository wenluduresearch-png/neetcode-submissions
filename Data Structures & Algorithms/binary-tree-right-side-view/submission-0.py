# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        l_ls = self.rightSideView(root.left)
        r_ls = self.rightSideView(root.right)
        return [root.val] + r_ls + l_ls[len(r_ls):]