def biggest_diff(nums):
    diff = 0 

    for num in nums:
        if length(nums) == 1:
            return 1
        elif length(nums) > 1:
            high = max(nums)
            low  = min(nums)
            diff = high - low
        return diff

nums = [3, 9, 4, 1, 0]
results = biggest_diff(nums)
print(results)            


