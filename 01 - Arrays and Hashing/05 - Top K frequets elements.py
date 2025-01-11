"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

import heapq
from typing import List


# Heap
def topKFrequentHeap(nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # A heap is used to track the k most frequent numbers.
    # A heap is a data structure that allows efficient access to the smallest element.
    # By default, Python heapq module creates a min-heap, meaning the smallest element is at the root (top) of the heap.

    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res


# Time complexity: O(n log k)
# Space complexity: O(n + k)


# Bucket Sort:


def topKFrequentBucket(nums: List[int], k: int):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# Time complexity: O(n)
# Space complexity: O(n)

print(topKFrequentBucket([1, 2, 2, 3, 3, 3], 2))
