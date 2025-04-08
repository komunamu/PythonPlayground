def isSubsequence(s: str, t: str) -> bool:
    # If s is empty, it's always a subsequence
    if not s:
        return True
    
    # If t is empty and s is not, s cannot be a subsequence
    if not t:
        return False
    
    # Pointer for string s
    s_pointer = 0
    
    # Iterate through t
    for char in t:
        # If current character matches, move s_pointer forward
        if char == s[s_pointer]:
            s_pointer += 1
            # If we've matched all characters in s, return True
            if s_pointer == len(s):
                return True
    
    # If we haven't matched all characters in s, return False
    return False

# Test cases
print(isSubsequence("abc", "ahbgdc"))  # True