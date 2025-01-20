def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    
    s1Count, s2Count = {}, {}
    for char in s1:
        s1Count[char] = s1Count.get(char, 0) + 1

    for i in range(len(s1)):
        s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

    matches = 0
    
    for char in s1Count:
        if s1Count[char] == s2Count.get(char, 0):
            matches += 1

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == len(s1Count):
            return True
        
        right_char = s2[r]
        s2Count[right_char] = s2Count.get(right_char, 0) + 1
        if s1Count.get(right_char, 0) == s2Count[right_char]:
            matches += 1
        elif s1Count.get(right_char, 0) + 1 == s2Count[right_char]:
            matches -= 1

        left_char = s2[l]
        s2Count[left_char] -= 1
        if s1Count.get(left_char, 0) == s2Count[left_char]:
            matches += 1
        elif s1Count.get(left_char, 0) - 1 == s2Count[left_char]:
            matches -= 1

        l += 1
    return matches == len(s1Count)

print(checkInclusion(s1 ="abc", s2 ="lecaabee"))