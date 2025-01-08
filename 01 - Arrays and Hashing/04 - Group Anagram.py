from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())


print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
