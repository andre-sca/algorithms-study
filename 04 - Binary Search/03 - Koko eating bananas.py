"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.
"""


import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 0, max(piles)
    res = r
    while l <= r:
        k = (1 + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res


print(minEatingSpeed([1, 4, 3, 2], 9))

# Time complexity: O(n * log m)

# Space complexity: O(1)
