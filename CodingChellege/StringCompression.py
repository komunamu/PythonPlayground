def compress(chars):
    if not chars:
        return 0
    if len(chars) == 1:
        return 1
    
    write_index = 0  # Position to write the compressed result
    count = 1        # Count of consecutive characters
    current_char = chars[0]
    
    # Iterate through array starting from second character
    for i in range(1, len(chars)):
        if chars[i] == current_char:
            # Same character, increment count
            count += 1
        else:
            # Different character, write the previous group
            write_index = write_group(chars, write_index, current_char, count)
            current_char = chars[i]
            count = 1
    
    # Write the last group
    write_index = write_group(chars, write_index, current_char, count)
    
    return write_index

def write_group(chars, index, char, count):
    # Write the character
    chars[index] = char
    index += 1
    
    # If count > 1, write the number
    if count > 1:
        # Convert count to string to handle multi-digit numbers
        count_str = str(count)
        for digit in count_str:
            chars[index] = digit
            index += 1
    
    return index

# Test cases
test1 = ["a","a","b","b","c","c","c"]
print(compress(test1), test1[:compress(test1)])  # Output: 6, ['a','2','b','2','c','3']

test2 = ["a"]
print(compress(test2), test2[:compress(test2)])  # Output: 1, ['a']

test3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(test3), test3[:compress(test3)])  # Output: 4, ['a','b','1','2']

test4 = ["a","a","a","b","b","a","a"]
print(compress(test4), test4[:compress(test4)])  # Output: 6, ['a','3','b','2','a','2']