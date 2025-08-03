# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is not a DFS problem!
        # this is a BFS problem - we need to code an iterative solution.
        if not root:
            return []

        queue = deque()
        res = []
        queue.append(root)
        while queue:
            between = []
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node:
                    between.append(current_node.val)
                    queue.append(current_node.left)
                    queue.append(current_node.right)
            if between:
                res.append(between)

        return res

            


