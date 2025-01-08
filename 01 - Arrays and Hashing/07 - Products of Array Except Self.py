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


productExceptSelf(nums=[-1, 1, 0, 2, 3])
