def gcdOfStrings(str1:str, str2:str) -> str:
    def divides(x: str, s:str) -> bool:
        if len(s) % len(x) != 0:
            return False
        times = len(s)//len(x)
        return x * times == s
    
    if str1 + str2 != str2 + str1:
        return ""
    
    def gcd(a: int, b: int) -> int:
        while b:
            a = b
            b = a % b
            #print(a)
            #print(b)
        
        return a
    
    gcd_length =gcd(len(str1), len(str2))
    
    print("gcd_length value:", gcd_length)
    return str1[:gcd_length]

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))
