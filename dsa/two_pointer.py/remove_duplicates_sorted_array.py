# Problem (simple)

# Given a sorted array, remove duplicates in-place so that each element appears only once.
# Return the count of unique elements.
# The first k elements of the array should contain the unique values.


def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # position for next unique element

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k
nums=list(map(int,input().split()))
print(removeDuplicates(nums))
print(nums)



# Correct step-by-step tracing

# Initial:

# nums = [0,0,1,1,1,2,2,3,3,4]
# k = 1

# i = 1
# nums[i] = 0
# nums[k-1] = nums[0] = 0
# 0 == 0 → skip
# k = 1

# i = 2
# nums[i] = 1
# nums[k-1] = nums[0] = 0
# 1 != 0 → copy
# nums[1] = 1
# k = 2


# Array:

# [0,1,1,1,1,2,2,3,3,4]

# i = 3
# nums[i] = 1
# nums[k-1] = nums[1] = 1
# 1 == 1 → skip
# k = 2

# i = 4
# nums[i] = 1
# nums[k-1] = nums[1] = 1
# 1 == 1 → skip
# k = 2

# i = 5
# nums[i] = 2
# nums[k-1] = nums[1] = 1
# 2 != 1 → copy
# nums[2] = 2
# k = 3


# Array:

# [0,1,2,1,1,2,2,3,3,4]

# i = 6
# nums[i] = 2
# nums[k-1] = nums[2] = 2
# 2 == 2 → skip
# k = 3

# i = 7
# nums[i] = 3
# nums[k-1] = nums[2] = 2
# 3 != 2 → copy
# nums[3] = 3
# k = 4


# Array:

# [0,1,2,3,1,2,2,3,3,4]

# i = 8
# nums[i] = 3
# nums[k-1] = nums[3] = 3
# 3 == 3 → skip
# k = 4

# i = 9
# nums[i] = 4
# nums[k-1] = nums[3] = 3
# 4 != 3 → copy
# nums[4] = 4
# k = 5


# Final array:

# [0,1,2,3,4,2,2,3,3,4]


# Return:

# k = 5