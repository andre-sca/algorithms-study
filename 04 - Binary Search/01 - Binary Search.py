"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (1 + r) // 2
        if nums[m] > target:
            r = m - 1
        if nums[m] < target:
            l = m + 1
        else:
            return m
    return -1