"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""

from typing import List


# Brute force
def twoSumBrute(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Time complexity: O(n2) -> nested loop.
# Space complexity: O(1)


# My own brute force
def twoSumTwoPersonalBrute(nums: List[int], target: int):
    for i, n in enumerate(nums):
        diff = target - n
        if diff in nums and nums.index(diff) != i:
            return [i, nums.index(diff)]


# Time complexity: O(n2) -> nested loop and a search in array (if diff in nums) which is O(n)
# Space complexity: O(1)


# One Pass, hash
def twoSumOnePass(nums: List[int], target: int):
    indices = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indices:
            return [indices[diff], i]
        indices[n] = i


# Time complexity: O(n) -> one loop. Search in dict (Hash table) is O(1).
# Space complexity: O(n) -> dict

print(twoSumBrute([3, 4, 5, 6], 7))
print(twoSumTwoPersonalBrute([3, 4, 5, 6], 7))
