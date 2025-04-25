def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    max_vowels = 0
    curr_vowels = 0
    
    # Count vowels in first window
    for i in range(k):
        if s[i] in vowels:
            curr_vowels += 1
    max_vowels = curr_vowels
    
    # Slide window and update max vowels
    for i in range(k, len(s)):
        # Add new character
        if s[i] in vowels:
            curr_vowels += 1
        # Remove character from start of previous window
        if s[i-k] in vowels:
            curr_vowels -= 1
        max_vowels = max(max_vowels, curr_vowels)
    
    return max_vowels

# Example usage:
print(maxVowels("abciiidef", 3))  # Output: 3
# Example usage:
print(maxVowels("aeiou", 2))      # Output: 2
