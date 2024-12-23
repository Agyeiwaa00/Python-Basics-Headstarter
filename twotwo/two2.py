# Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the resulting numbers that end in 2.

# two2([1, 2, 3]) → [4, 6]
# two2([2, 6, 11]) → [4]
# two2([0]) → [0]

def two2(nums):
    # Multiply each number by 2 and filter out those ending in 2
    return [num * 2 for num in nums if (num * 2) % 10 != 2]

# Test cases
print(two2([1, 2, 3]))  # → [4, 6]
print(two2([2, 6, 11]))  # → [4]