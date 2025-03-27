def canPlaceFlowers(flowerbed: list[int], n: int)-> bool:
    # Add 0s at the beginning and end to handle edge cases easily
    flowerbed = [0] + flowerbed + [0]
    count = 0  # Counter for possible new flowers
    
    # Iterate through the flowerbed, excluding the extra 0s we added
    for i in range(1, len(flowerbed) - 1):
        # Check if current plot is empty and both adjacent plots are empty
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1  # Plant a flower
            count += 1  # Increment counter
    
    # Return true if we can plant n or more flowers
    return count >= n

print(canPlaceFlowers([1,0,0,0,1], 1))  # True
print(canPlaceFlowers([1,0,0,0,1], 2))  # False

# Example usage:
# flowerbed = [1,0,0,0,1], n = 1 -> returns True
# flowerbed = [1,0,0,0,1], n = 2 -> returns False