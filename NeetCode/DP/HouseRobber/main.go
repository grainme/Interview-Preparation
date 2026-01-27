func helper(nums, dp []int, k int) int {
    if dp[k] != -1 {
        return dp[k]
    }
    if k < 2 {
        return nums[k]
    }

    mx := nums[k]
    for i := k-2; i >= 0; i-- {
        mx = max(mx, nums[k] + helper(nums, dp, i))
    }

    dp[k] = mx
    return mx
}

func rob(nums []int) int {
    mx_ever := 0
    dp := make([]int, len(nums))
    for i, _ := range dp {
        dp[i] = -1
    }

    for i := len(nums) - 1; i >= 0; i-- {
        mx_ever = max(mx_ever, helper(nums, dp, i))
    } 

    return mx_ever
}
