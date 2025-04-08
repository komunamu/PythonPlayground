def maxArea(height):
    left = 0;
    right = len(height) - 1
    max_area = 0
    # Initialize max_area to 0
    while left < right:
        # Calculate the width
        width = right - left
        # Calculate the height
        h = min(height[left], height[right])
        # Calculate the area
        area = width * h
        # Update max_area if the current area is larger
        max_area = max(max_area, area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
# Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output: 49
# Example usage:
height = [1,1]
print(maxArea(height))  # Output: 1
# Example usage:
height = [4,3,2,1,4]
print(maxArea(height))  # Output: 16
# Example usage:
height = [1,2,1]
print(maxArea(height))  # Output: 2