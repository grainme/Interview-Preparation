"""
Find the majority element in an array (one that appears more than n/2 times)
in O(n) time and O(1) space without hashmaps.

Example:
> majorityElement([2, 2, 1, 1, 2, 2, 1, 2, 2])
2

> majorityElement([3, 3, 4, 2, 3, 3, 1])
3

"""

from typing import List


# Boyer-Moore Voting algorithm
def majorityElement(arr: List[int]) -> int:
    m = -1
    c = 0
    for e in arr:
        if c == 0:
            m = e
            c += 1
        elif e == m:
            c += 1
        else:
            c -= 1
    return m


def main():
    res = majorityElement([2, 2, 1, 1, 2, 2, 1, 2, 2])
    print(res)

    res = majorityElement([3, 3, 4, 2, 3, 3, 1])
    print(res)


if __name__ == "__main__":
    main()
