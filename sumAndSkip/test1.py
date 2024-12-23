
def biggest_diff(nums):
    diff = 0 

    if len(nums) == 1:
            return 1
    elif len(nums) > 1:
            high = max(nums)
            low  = min(nums)
            diff = high - low
    elif len(nums) == 0:    
        print("array is empty")
    return diff       

nums = [3, 9, 4, 1, 6]
results = biggest_diff(nums)
print(results)   

# Alternative Result
# Check if the list is not empty and has more than one element
#if nums and len(nums) > 0:
        # Find the maximum and minimum values in the list
       # max_val = max(nums)
       # min_val = min(nums)
        # Calculate the difference between the maximum and minimum values
    #return max_val - min_val
#else:
#        return 0  # Return 0 if the list is empty or not provided


