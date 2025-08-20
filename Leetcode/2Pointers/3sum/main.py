class Solution:
    # You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sz = len(nums)
        res = []
        st = set()
        for i in range(sz):
            j = i + 1
            k = sz - 1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if i != j and j != k and i != k and sm == 0:
                    if (nums[i], nums[j], nums[k]) not in st:
                        res.append([nums[i], nums[j], nums[k]])
                    st.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif sm > 0:
                    k -= 1
                else:
                    j += 1
        return res
