"""
You are given a string s consisting of lowercase English letters. Find the length of the longest substring that contains at most two distinct characters.

Input:
s = "eceba"
Output:
3
Explanation: The substring "ece" contains only two distinct characters.
"""

def length_of_longest_substring_two_distinct(s):
    left = 0
    right = 0
    char_count = {}
    distinct_count = 0
    longest = 0

    while right < len(s):
        # Add the character at `right` to the map
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        # If it's the first occurrence, increase distinct count
        if char_count[s[right]] == 1:
            distinct_count += 1

        # Shrink the window if there are more than two distinct characters
        while distinct_count > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                distinct_count -= 1
                del char_count[s[left]]
            left += 1

        # Update the longest substring length
        longest = max(longest, right - left + 1)
        right += 1

    return longest

def length_of_longest_substring_two_distinct(s):
    left = 0
    char_count = {}
    longest = 0

    for right in range(len(s)):
        # Add the character at `right` to the map
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Shrink the window until we have at most 2 distinct characters
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update the longest substring length
        longest = max(longest, right - left + 1)

    return longest





print(length_of_longest_substring_two_distinct("eceba"))
print(length_of_longest_substring_two_distinct("aaaaaabc"))
print(length_of_longest_substring_two_distinct("eccebbaaaa"))