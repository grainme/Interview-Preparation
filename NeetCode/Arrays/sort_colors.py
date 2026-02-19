from typing import List


# this is medium BTW
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = [0] * 3
        for e in nums:
            arr[e] += 1

        k = 0
        for e in range(3):
            for i in range(arr[e]):
                nums[k] = e
                k += 1
