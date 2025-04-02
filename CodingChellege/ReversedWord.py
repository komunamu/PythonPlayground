def reverseWords(self, s: str) -> str:
       words = s.split()
       reversed_words= words[::-1]
       return " ".join(reversed_words)
   
s = "Hello World"
print(reverseWords(None, s))
# Output: "World Hello"