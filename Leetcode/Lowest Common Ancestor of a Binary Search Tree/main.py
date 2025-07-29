# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lca = None

    def inTree(self, root: TreeNode, node: TreeNode) -> bool:
        if not root and not node:
            return root
        if not root and node:
            return None
        if root.val == node.val:
            return root
        left = self.inTree(root.left, node)
        right = self.inTree(root.right, node)
        return right or left

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if self.inTree(root, p) and self.inTree(root, q):
            self.lca = root
        self.lowestCommonAncestor(root.left, p, q)
        self.lowestCommonAncestor(root.right, p, q)
        return self.lca
