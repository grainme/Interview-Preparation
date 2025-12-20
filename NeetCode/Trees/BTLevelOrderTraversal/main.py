from collections import deque
from turtle import resetscreen
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        result = []
        q.append(root)
        while q:
            qSz = len(q)
            level = []
            for i in range(qSz):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            result.append(level)
        return result
