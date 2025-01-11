"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

from typing import List


# Brute Force
def hasDuplicate(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# Time complexity: O(n2) -> nested loops, one inside the other.
# Space complexty: O(1) -> i and j are the loop variables, both of which take constant space (O(1) each).


# Hash Set
def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


# Time complexity: O(n) -> one loop
# Space complexity: O(n) -> one set of n elements.


print(hasDuplicate([1, 2, 3, 3]))
print(containsDuplicate([1, 2, 3, 3]))
