# credits: https://leetcode.com/problems/subtree-of-another-tree/solutions/6723566/master-subtree-detection-with-tree-serialization/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def ser(n: TreeNode) -> str:
            if not n:
                return ",#"
            return "," + str(n.val) + ser(n.left) + ser(n.right)
        return ser(subRoot) in ser(root)
