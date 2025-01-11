"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
"""

# Sorting:


def isAnagramSorting(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


# Time Complexity: O(n log n + m log m) if they are different sizes, however, for the script to run fully
#   they will be of the same size, leading to O(n log n)
# Space Complexity: O(1) or O(n + m)


# Hash
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


# Time Complexity: O(n + m)
# Space Complexity: O(1)


print(isAnagramSorting("racecar", "carrace"))
print(isAnagram("racecar", "carrace"))
