#House Robber-1
        # def rob(nums):
        #     r1,r2=0,0
        #     for i in nums:
        #         temp=max(i+r1,r2)
        #         r1=r2
        #         r2=temp
        #     return r2
        # nums=[2,7,9,3,1]
        # print(rob(nums))



#House Robber-2
# def rob(nums):
#     def helper(nums):
#         r1,r2=0,0
#         for i in nums:
#             temp=max(i+r1,r2)
#             r1=r2
#             r2=temp
#         return r2
#     return max(helper(nums[1:]),helper([nums[:-1]]))
# nums=[2,7,9,3,1]
# print(rob(nums))
