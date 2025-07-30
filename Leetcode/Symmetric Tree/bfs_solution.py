# I'm proud of this solution becuae of line 25 lol :)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # is this: invert problem + same problem?
        # or maybe run a BFS and create a list based on the level?
        q = collections.deque()
        q.append(root)
        while q:
            bet = []
            lQueue = len(q)
            for _ in range(lQueue):
                node = q.popleft()
                if node:
                    bet.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
                else:
                    bet.append(-200)
            for i in bet:
                print(i)
            if bet:
                l = len(bet)
                for i in range(l//2):
                    if bet[i] != bet[l-i-1]:
                        return False

        return True
