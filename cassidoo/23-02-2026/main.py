"""
this week's question:
Given an array of integers, find the contiguous subarray that has the largest sum and return that sum. 

A subarray must contain at least one element. 

If all elements are negative, return the largest (least negative) value. 

> If you need a hint, look up Kadane's Algorithm!

Examples:

> maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
6
> maxSubarraySum([5])
5
> maxSubarraySum([-1, -2, -3, -4])
-1
> maxSubarraySum([5, 4, -1, 7, 8])
23
"""

from typing import List


def maxSubarraySum(arr: List[int]) -> int:
    mx_ever = arr[0]
    sum_so_far = arr[0]
    
    for e in arr[1:]:
        if e >= sum_so_far and sum_so_far < 0:
            sum_so_far = e
        else:
            sum_so_far += e
        mx_ever = max(mx_ever, sum_so_far)
        
    return mx_ever


def main():
    res = maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(res)
    
    res = maxSubarraySum([5])
    print(res)
    
    res = maxSubarraySum([-1, -2, -3, -4])
    print(res)
    
    res = maxSubarraySum([5, 4, -1, 7, 8])
    print(res)


if __name__ == "__main__":
    main()
