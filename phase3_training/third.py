#group Anagrams

        # strs = ["eat","tea","tan","ate","nat","bat"]
        # dic={}
        # for word in strs:
        #     word_sort=sorted(word)
        #     key="".join(word_sort)
        #     # dic[word_sort_str]=dic.get(word_sort_str,[])+[word]
        #     if key in dic:
        #         dic[key].append(word)
        #     else:
        #         dic[key]=[word]
        # print(list(dic.values()))

# -----------------------------------------------------------------------------------------------------------------------
#Longest Consecutive Sequence

        # nums = [100,4,200,1,5,3,2]
        # max_len=0
        # hash_map=set(nums)
        # for num in hash_map:
        #     if (num-1) not in hash_map:
        #         count=1
        #         while (count+num) in hash_map:
        #              count+=1
        #         max_len=max(count,max_len)
        # print(max_len)
# -----------------------------------------------------------------------------------------------------------------------
#Palindrome

        # n=123521
        # st=str(n)
        # print(st==st[::-1])


        # n=12321
        # temp=n
        # res=0
        # while n:
        #         digit=n%10
        #         res=res*10+digit
        #         n//=10
        # print(temp==res)


        # #using 2 pointer
        # n="madam"
        # i=0
        # j=len(n)-1
        # while i<j:
        #     if n[i]!=n[j]:
        #         print("not a palindrome")
        #         break
        #     i+=1
        #     j-=1
        # else:
        #     print("Palindrome")

# ---------------------------------------------------------------------------------------------------------------------------
#subarray sum equals k

        # nums=[1,1,1,-1,2,-2]
        # k=2
        # hash_map={0:1}
        # pref_sum=0
        # res=0
        # for num in nums:
        #     pref_sum+=num
        #     temp=pref_sum-k
        #     res+=hash_map.get(temp,0)
        #     hash_map[pref_sum]=hash_map.get(pref_sum,0)+1
        # print(res)

# --------------------------------------------------------------------------------------
#3 Sum (3 pointers)

#Brute Force

        # def threeSum(nums):
        #         n = len(nums)
        #         ans = []
        #         for i in range(n):
        #                 for j in range(i + 1, n):
        #                         for k in range(j + 1, n):
        #                                 if nums[i] + nums[j] + nums[k] == 0:
        #                                         triplet = sorted([nums[i], nums[j], nums[k]])
        #                                         if triplet not in ans:
        #                                                 ans.append(triplet)
        #         return ans
        # nums=[-1,0,1,2,-1,-4]
        # print(threeSum(nums))


        # nums=[-1,0,1,2,-1,-4]
        # nums=[0,0,0,0]
        # res=[]
        # nums.sort()
        # n=len(nums)
        # for i in range(n-2):
        #         if i!=0 and nums[i]==nums[i-1]:
        #             continue
        #         j=i+1
        #         k=n-1
        #         while j<k:
        #                 triplet=nums[i]+nums[j]+nums[k]
        #                 if triplet==0:
        #                         res.append([nums[i],nums[j],nums[k]])
        #                         j+=1
        #                         k-=1
        #                 elif triplet>0:
        #                         k-=1
        #                 else:
        #                         j+=1
        #         while j<k and nums[j]==nums[j+1]:
        #                 j+=1
        # print(res)

# ----------------------------------------------------------------------------------------------
#Reverse list using 2 pointer technique

        # nums=[1,2,4,3,6,7]
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     nums[i],nums[j]=nums[j],nums[i]
        #     i+=1
        #     j-=1
        # print(nums)
# --------------------------------------------------------------------------------------------------------------------------
#Two sum-2 give array is sorted(using 2 pointers)

        # nums=[1,7,26,12,2,23]
        # tar=9
        # i=0
        # j=len(nums)-1
        # while True:
        #         sm=nums[i]+nums[j]
        #         if sm==tar:
        #                 print([i+1,j+1])
        #                 break
        #         elif sm>tar:
        #                 j-=1
        #         else:
        #                 i+=1
# --------------------------------------------------------------------------------------------------------------------------
