class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sz = len(cost)
        dp = [None] * (sz + 2)
        
        def helper(ind: int) -> int:
            nonlocal cost, sz, dp
            if dp[ind] is not None:
                return dp[ind]
            if ind >= sz:
                return 0
            dp[ind] = min(cost[ind] + helper(ind + 1), cost[ind] + helper(ind + 2))
            return dp[ind]

        return min(helper(0), helper(1))

