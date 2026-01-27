func rob(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    if n == 1 {
        return nums[0]
    }

    dp := make([]int, n)
    for i, _ := range dp {
        dp[i] = -1
    }

    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i := 2; i < n; i++ {
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    }

    return dp[n-1]
}
