# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def good(self, root: TreeNode, max_so_far: int) -> int:
        if not root:
            return 0
        if root.val >= max_so_far:
            max_so_far = root.val
            self.ans += 1

        self.good(root.right, max_so_far)
        self.good(root.left, max_so_far)

    def goodNodes(self, root: TreeNode) -> int:
        self.good(root, root.val)
        return self.ans
        
