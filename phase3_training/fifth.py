#Sliding Window
# 1) maximum points you can obtain from cards

# def max_Score(cardPoints,k):
#     n=len(cardPoints)
#     l=0
#     total=sum(cardPoints[n-k:])
#     res=total
#     for r in range(n-k,n):
#         total+=cardPoints[l]-cardPoints[r]
#         res=max(res,total)
#         l+=1
#     return res
# cardPoints = [1,2,3,4,5,6,1]
# k=3
# print(max_Score(cardPoints,k))

# ----------------------------------------------------------------------------------------------------------

