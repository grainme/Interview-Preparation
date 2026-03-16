from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def KthSmallest(root: Optional[TreeNode], k: int) -> int:
        res = -1

        def dfs(root: Optional[TreeNode]):
            nonlocal res, k
            if not root:
                return

            dfs(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            dfs(root.right)

        dfs(root)
        return res


def main():
    left = TreeNode(1, None, None)
    right = TreeNode(3, None, None)
    root = TreeNode(2, left, right)

    res = Solution.KthSmallest(root, 1)
    print(res)


if __name__ == "__main__":
    main()
