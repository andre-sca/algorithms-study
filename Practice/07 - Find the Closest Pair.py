"""
Given two sorted arrays nums1 and nums2 of lengths m and n respectively, and a target value, find the pair of numbers (one from each array) whose sum is closest to the target.

Input:
nums1 = [1, 4, 5, 7], nums2 = [10, 20, 30, 40], target = 32
Output:
[1, 30]
Explanation: The sum 1 + 30 = 31 is closest to the target 32.
"""

def findClosestPair(nums1: list, nums2: list, target: int):
    i, j = 0, len(nums2) - 1
    minDiff = float('inf')
    closestPair = (0, 0)  # To store the pair

    while i < len(nums1) and j >= 0:
        currentSum = nums1[i] + nums2[j]
        currentDiff = abs(currentSum - target)

        # Update closest pair if current difference is smaller
        if currentDiff < minDiff:
            minDiff = currentDiff
            closestPair = (nums1[i], nums2[j])

        # Adjust pointers based on comparison with target
        if currentSum > target:
            j -= 1
        elif currentSum < target:
            i += 1
        else:  # If exactly equal to the target, return immediately
            return (nums1[i], nums2[j])

    return closestPair




print(findClosestPair([5, 6, 7, 8], [1, 2, 3], 10))
