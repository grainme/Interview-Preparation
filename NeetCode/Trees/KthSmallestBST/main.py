# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # this a BST, which means => ( root >= left && root <= right) 
        cnt = 0
        res = root.val
        def dfs(root: TreeNode):
            nonlocal cnt
            nonlocal res
            if root is None:
                return
            dfs(root.left)
            cnt += 1
            if cnt == k:
                res = root.val
                return
            dfs(root.right)

        dfs(root)
        return res
