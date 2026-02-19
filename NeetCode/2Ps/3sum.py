from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm == 0:
                    trio = sorted([nums[i], nums[j], nums[k]])
                    res.add(tuple(trio))
                    j += 1
                    k -= 1
                elif sm > 0:
                    k -= 1
                else:
                    j += 1

        r = []
        for t in res:
            r.append(list(t))
        return r
