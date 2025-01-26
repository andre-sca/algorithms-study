def validPalindrome(s: str):
    left, right = 0, len(s) - 1
    hasRemoved = False

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if not hasRemoved and s[left] == s[right -1]:
                right -= 1
                hasRemoved = True
            elif not hasRemoved and s[left + 1] == s[right]:
                hasRemoved = True
                left += 1
            else:
                return False
    return True


print(validPalindrome('abca'))
print(validPalindrome('abc'))
print(validPalindrome('abbca'))