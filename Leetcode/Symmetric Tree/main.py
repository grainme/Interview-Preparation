# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> None:
        if not root: 
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

    def sameTree(self, root: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
        if not root and not other:
            return True
        if (not root and other) or (root and not other):
            return False
        return root.val == other.val and self.sameTree(root.left, other.left) and self.sameTree(root.right, other.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # is this: invert problem + same problem?
        self.invertTree(root.right)
        return self.sameTree(root.left, root.right)
