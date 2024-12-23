# Given an array of ints, determine if it is possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen.

# groupNoAdj(0, [2, 5, 10, 4], 12) → true
# groupNoAdj(0, [2, 5, 10, 4], 14) → false
# groupNoAdj(0, [2, 5, 10, 4], 7) → false


def groupNoAdj(start, nums, target):
    # Base case: If the target is 0, the condition is met
    if target == 0:
        return True
    # Base case: If we reach the end of the array without meeting the target
    if start >= len(nums):
        return False

    # Recursive step:
    # 1. Include nums[start] in the group and skip the next value
    if groupNoAdj(start + 2, nums, target - nums[start]):
        return True
    # 2. Exclude nums[start] from the group
    if groupNoAdj(start + 1, nums, target):
        return True

    # If neither option works, return False
    return False

# Test cases
print(groupNoAdj(0, [2, 5, 10, 4], 12))  # → True
print(groupNoAdj(0, [2, 5, 10, 4], 14))  # → False
print(groupNoAdj(0, [2, 5, 10, 4], 7))   # → False