class Solution:
    def __init__(self):
        self.dp = [0 for _ in range(47)]

    def climbStairs(self, n: int) -> int:
        if self.dp[n] > 0:
            return self.dp[n]
        if n == 0:
            return 1
        
        left = 0
        right = 0
        if n - 1 >= 0:
            left = self.climbStairs(n-1)
        if n - 2 >= 0:
            right = self.climbStairs(n-2)
        # cache the computation
        self.dp[n] = left + right

        return left + right
