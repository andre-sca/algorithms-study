"""Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array."""

from typing import List


# Hash set
def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))

# Time complexity: O(n)

# Space complexti: 0(n)
