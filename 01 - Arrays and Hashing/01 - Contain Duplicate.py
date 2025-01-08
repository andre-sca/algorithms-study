from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(containsDuplicate([1, 2, 3, 3]))
