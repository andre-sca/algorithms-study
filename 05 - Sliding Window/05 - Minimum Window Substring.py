def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ''
    
    sHash, tHash = {}, {}

    # Build t hash
    for char in t:
        tHash[char] = tHash.get(char, 0) + 1
    
    # Build s hash for size o t
    for i in range(len(t)):
        sHash[s[i]] = sHash.get(s[i], 0) + 1

    # Populate matches
    matches = 0
    for char in tHash:
        if tHash[char] == sHash.get(char, 0):
            matches += 1

    l = 0
    r = len(t)
    res = ''
    while l < r:

        if matches < len(t):
            if r > len(s) - 1:
                break

            right_char = s[r]
            sHash[right_char] = sHash.get(right_char, 0) + 1
            
            if sHash[right_char] == tHash.get(right_char, ''):
                matches += 1
            elif tHash.get(right_char) and sHash[right_char] < tHash.get(right_char, 0):
                matches -= 1
            
            r += 1

        elif matches >= len(t):
            res = s[l:r] if len(s[l:r]) < len(res) or res == '' else res
            
            left_char = s[l]
            sHash[left_char] -= 1
            if tHash.get(left_char) and sHash[left_char] < tHash.get(left_char, 0):
                matches -= 1
            
            l += 1
    return res

print(minWindow(s="a", t="aa"))