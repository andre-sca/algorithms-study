"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.
"""


def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n  # Initialize output array with 1s

    # Prefix pass
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Suffix pass
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output


# Time complexity: O(n)

# Space complexity: 0(1)


productExceptSelf(nums=[-1, 1, 0, 2, 3])
