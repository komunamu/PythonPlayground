def findMaxAverage(nums: list[int], k: int) -> float:
    # Get sum of first k elements
    curr_sum = sum(nums[:k])
    # Initialize max_sum as the first window sum
    max_sum = curr_sum
    
    # Slide window and update max_sum
    for i in range(k, len(nums)):
        # Add new element and remove first element of previous window
        curr_sum = curr_sum + nums[i] - nums[i-k]
        max_sum = max(max_sum, curr_sum)
    
    # Return maximum average
    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
print("num: "+findMaxAverage(nums, k))  # Output: 12.75