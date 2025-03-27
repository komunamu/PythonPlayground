def kidWithCandies(candies: list[int], extraCandies: int) -> list[bool] :
    # find the maximum number of candies any kid currently has
    max_candy = max(candies)
    
    #for each kid, check if their candies plus extra would equal or exceed the maximum 
    result = []
    for candy in candies:
        if candy + extraCandies >= max_candy:
            result.append(True)
        else:
            result.append(False)
            
    return result

print(kidWithCandies([3,4,5,2,3], 3))


    
    