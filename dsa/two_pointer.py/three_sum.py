# 3 Sum Problem (Using Two Pointers)

# Problem Statement

# Given an integer array nums, find all unique triplets (i, j, k) such that:
# i ≠ j ≠ k
# nums[i] + nums[j] + nums[k] = 0
# The solution set must not contain duplicate triplets

# Example

# Input:
# nums = [-1, 0, 1, 2, -1, -4]

# Output:

# [[-1, -1, 2],
#  [-1,  0, 1]]


def three_sum(nums):
    nums.sort()
    res=[]
    n=len(nums)
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,n-1
        while l<r:
            tot=nums[i]+nums[l]+nums[r]
            if tot==0:
                res.append([nums[i],nums[l],nums[r]])
                # skip duplicates
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
            elif tot<0:
                l+=1
            else:
                r-=1
    return res

nums=list(map(int,input().split()))
print(three_sum(nums))    


# 3. Three Sum (Brute Force)
# Problem

# Check if any three numbers sum to target.

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in ans:
                            ans.append(triplet)
        return ans