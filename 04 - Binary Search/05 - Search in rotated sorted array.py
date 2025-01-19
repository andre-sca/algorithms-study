from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (r + l) // 2
        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = l + 1
            else:
                r = r - 1
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1


print(search([3, 4, 5, 6, 1, 2], 1))
