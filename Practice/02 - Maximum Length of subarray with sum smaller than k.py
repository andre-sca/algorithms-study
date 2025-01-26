def maximumSumSmallerThanK(nums: list, k: int):
    left, right = 0, 0
    maxSumLen = 0
    current_sum = 0

    while right < len(nums):
        current_sum += nums[right]

        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1
        maxSumLen = max(maxSumLen, right - left + 1)
        right += 1
    return maxSumLen
        



print(maximumSumSmallerThanK([3, 1, 2, 7, 4, 2], 8))