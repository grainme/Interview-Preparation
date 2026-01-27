func rob(nums []int) int {
    n := len(nums)
    dp := make([]int, n)
    for i, _ := range dp {
        dp[i] = -1
    }

    var dfs func(k int) int
    dfs = func(k int) int {
        if k < 0 {
            return 0
        }
        if dp[k] != -1 {
            return dp[k]
        }

        dp[k] = max(dfs(k-1), nums[k] + dfs(k-2))
        return dp[k]
    }

    return dfs(n-1)
}
