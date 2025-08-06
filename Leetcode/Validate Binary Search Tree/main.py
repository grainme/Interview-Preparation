# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # In this solution I used space - we can do better!!
    def __init__(self):
        self.arr = []
        
    def validate(self, node: TreeNode):
        if not node:
            return
        self.validate(node.left)
        self.arr.append(node.val)
        self.validate(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.validate(root)
        for i in range(len(self.arr)-1):
            if self.arr[i+1] - self.arr[i] <= 0:
                return False
        return True
        
