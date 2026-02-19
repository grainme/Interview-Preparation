# we need to solve the problem in O(NlogN)
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        first_half = self.sortArray(nums[: len(nums) // 2])
        second_half = self.sortArray(nums[len(nums) // 2 :])

        return self.merge(first_half, second_half)

    def merge(self, first: List[int], second: List[int]):
        sorted_list = []
        i = 0
        j = 0
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                sorted_list.append(first[i])
                i += 1
            else:
                sorted_list.append(second[j])
                j += 1

        while i < len(first):
            sorted_list.append(first[i])
            i += 1
        while j < len(second):
            sorted_list.append(second[j])
            j += 1
        return sorted_list


# Testing
def main():
    solution = Solution()
    arr = [5, 2, 3, 1]

    sort_arr = solution.sortArray(arr)
    print("Sorted Array: ", sort_arr)


if __name__ == "__main__":
    main()
