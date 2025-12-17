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
    def __init__(self) -> None:
        self.maxDiameter = 0

    def heightDFS(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        leftHeight = self.heightDFS(node.left)
        rightHeight = self.heightDFS(node.right)
        self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)

        return max(leftHeight, rightHeight) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.heightDFS(root)
        return self.maxDiameter
