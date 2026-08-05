# Problem Statement (simple)

# Given an array nums and an integer target, pick three numbers such that their sum is closest to target.
# Return the sum, not the triplet.

# There is exactly one answer.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        clos_sum=nums[0]+nums[1]+nums[2]
        n=len(nums)
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                cur_sum=nums[i]+nums[l]+nums[r]
                if abs(cur_sum-target)<abs(clos_sum-target):
                    clos_sum=cur_sum
                elif cur_sum<target:
                    l+=1
                elif cur_sum>target:
                    r-=1
                else:
                    return target
        return clos_sum
