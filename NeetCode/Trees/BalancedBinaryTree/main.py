# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxDiff = 0

        def depth(root: Optional[TreeNode]) -> int:
            nonlocal maxDiff
            if root is None:
                return 0
            leftDepth = depth(root.left)
            rightDepth = depth(root.right)
            maxDiff = max(maxDiff, abs(leftDepth - rightDepth))
            return max(leftDepth, rightDepth) + 1

        if root is None:
            return True
        depth(root)
        return maxDiff < 2
