# Lets say that a value is "everywhere" in an array if for every pair of adjacent elements in the array, at least one of the pair is that value. 
# Return true if the given value is everywhere in the array.


# isEverywhere([1, 2, 1, 3], 1) → true
# isEverywhere([1, 2, 1, 3], 2) → false
# isEverywhere([1, 2, 1, 3, 4], 1) → false

def isEverywhere(nums, val):
    
    for i in range(len(nums)- 1):
        if nums[i]!= val and nums[i+1] != val:
            return False
    return True  

test1 = isEverywhere([1, 2, 2, 4], 2)
test2 = isEverywhere([1, 2, 1, 3], 3)
print(test1, test2)