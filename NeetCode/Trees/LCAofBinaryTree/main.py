from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
class Solution:
    def __init__(self):
        self.lca = None

    def containsNode(self, root: Optional[TreeNode], node: TreeNode) -> bool:
        if not root:
            return False
        if root.val == node.val:
            return True
        right = self.containsNode(root.right, node)
        left = self.containsNode(root.left, node)
        return right or left

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> Optional[TreeNode]:
        contains = self.containsNode(root, p) and self.containsNode(root, q)
        if contains:
            self.lca = root
        if root.left:
            self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            self.lowestCommonAncestor(root.right, p, q)
        return self.lca
