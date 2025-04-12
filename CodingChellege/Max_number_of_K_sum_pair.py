def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    operations = 0
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == k:
            operations += 1
            left += 1
            right -= 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1
            
    return operations

maxOperations([1, 2, 3, 4], 5)  # Output: 2