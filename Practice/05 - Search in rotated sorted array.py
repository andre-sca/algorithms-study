def searchRotatedArray(nums: list, target: int):
    left, right = 0, len(nums) - 1

    while left <= right:
        m = (right + left) // 2
        if nums[m] == target:
            return m

        if nums[left] < target:
            if nums[left] <= target < nums[m]:
                right = m - 1
            else:
                left = m + 1
        else:
            if nums[m] < target <= nums[right]:
                left = m + 1
            else:
                right = m - 1
    return -1




print(searchRotatedArray([5, 6, 7, 0, 1, 2, 4], 2))