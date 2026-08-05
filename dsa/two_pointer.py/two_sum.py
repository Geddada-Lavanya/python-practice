# TWO SUM
# Problem Statement

# Given an array of integers arr and an integer target, find two different elements in the array such that their sum is equal to target.
# Example

# Input:
# arr = [2, 7, 11, 15]
# target = 9

# Output:
# [2,7]
# Explanation: 2 + 7 = 9


def two_sum(arr,target):
    arr.sort()
    l,r=0,len(arr)-1
    while l<r:
        curr_sum=arr[l]+arr[r]
        if curr_sum==target:
            return [arr[l],arr[r]]
        elif curr_sum>target:
            r-=1
        else:
            l+=1
    return "no pair found"
arr=list(map(int,input().split()))
target=int(input())
print(two_sum(arr,target))




# Two Sum – Return Indices (Using Two Pointers)

# Problem Statement

# Given an array arr and an integer target, return the indices of two elements such that their sum equals target.
# Each element can be used only once.

def twoSum(arr, target):
    nums = [(arr[i], i) for i in range(len(arr))]
    nums.sort(key=lambda x: x[0])

    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left][0] + nums[right][0]

        if curr_sum == target:
            return [nums[left][1], nums[right][1]]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return "No solution"


# -------------------------------------------------------------------------------------------------

# using nested for loop 

def twoSum(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]

    return "No solution"
