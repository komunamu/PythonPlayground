def moveZeroes(nums):
    # Position to place the next non-zero element
    non_zero_pos = 0
    
    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            print(nums , non_zero_pos, i)
            
            non_zero_pos += 1
    
    return nums

test1 = [0,1,0,3,12]
print(moveZeroes(test1))  # Output: [1,3,12,0,0]
