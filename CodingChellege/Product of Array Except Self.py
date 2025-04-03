def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
    
    print(output)

    # Calculate the prefix products
    prefix_product = 1
    for i in range(n):
        output[i] = prefix_product
        prefix_product *= nums[i]
        print(output)
        print(prefix_product)

    # Calculate the suffix products and multiply with the prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= nums[i]

    return output

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
# Example usage:
# nums = [1, 2, 3, 4] -> returns [24, 12, 8, 6]