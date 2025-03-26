#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.




def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i=0
    while i<len(word1) or i<len(word2):
        if i<len(word1):
            merged.append(word1[i])
            
        if i<len(word2):
            merged.append(word2[i])
            
        i += 1
        print(merged)
        
    return ''.join(merged)
    

word1= "abc"
word2= "defght"

print(mergeAlternately(word1, word2))

