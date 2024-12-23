# Given an array of ints, return a boolean to determine if it is possible to divide the ints into two groups, so that the sums of the two groups are the same. 
# Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitArray(). 

# splitArray([2, 2]) → true
# splitArray([2, 3]) → false
# splitArray([5, 2, 3]) → true

def splitArray(nums):
    def helper(index, sum1, sum2):
        # Base case: if we've checked all numbers
        if index == len(nums):
            return sum1 == sum2
        
        # Recursive case: Try including the current number in either of the two groups
        return helper(index + 1, sum1 + nums[index], sum2) or helper(index + 1, sum1, sum2 + nums[index])
    
    # Initial call to the helper function
    return helper(0, 0, 0)

# Example usage
print(splitArray([1, 2, 3, 4]))  # Output: True
print(splitArray([1, 1, 1, 2, 2]))  # Output: True
print(splitArray([1, 2, 3, 5]))  # Output: False
