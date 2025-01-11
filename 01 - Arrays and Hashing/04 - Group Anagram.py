"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

from collections import defaultdict
from typing import List


# Sorting:
def groupAnagramsSort(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        sortedS = "".join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())


# Time complexity: O(n * m log m)
# Space complexity: O(n * m)


# Hash
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())


print(groupAnagramsSort(["act", "pots", "tops", "cat", "stop", "hat"]))
print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))

# Time complexity: O(m * n)
# Space complexity: O(m)
