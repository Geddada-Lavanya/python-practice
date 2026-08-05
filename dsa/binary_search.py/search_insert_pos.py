# Problem Statement

# You are given a sorted array and a target value.
# If the target is found, return its index.
# If not found, return the index where it should be inserted to keep the array sorted.

# Example
# nums = [1,3,5,6], target = 5 → Output: 2
# nums = [1,3,5,6], target = 2 → Output: 1


def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
