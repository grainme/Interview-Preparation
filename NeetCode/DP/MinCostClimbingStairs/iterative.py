func minCostClimbingStairs(cost []int) int {
    sz := len(cost)
    dp := make([]int, sz + 1)

    // dp[i] is the cost to get to "i"
    dp[0], dp[1] = 0, 0 // we can get these for free based on the prob statement

    for i := 2; i <= sz; i++ {
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    }

    return dp[sz]
}

