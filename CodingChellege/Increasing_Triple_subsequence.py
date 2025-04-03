def increasingTriplet(nums):
    # Initialize first and second numbers of the triplet
    first = float('inf')  # Smallest number seen so far
    second = float('inf') # Second smallest number seen so far
    
    for num in nums:
        # If current number is smaller than first, update first
        if num <= first:
            first = num
        # If current number is greater than first but smaller than second, update second
        elif num <= second:
            second = num
        # If current number is greater than both first and second, we found a triplet
        else:
            return True
            
    return False