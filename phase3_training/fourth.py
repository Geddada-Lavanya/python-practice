#Container with most Water

# Brute Force
        # height=[1,8,6,2,5,4,8,3,7]
        # max_area=0
        # n=len(height)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         h=min(height[i],height[j])
        #         w=j-i
        #         area=h*w
        #         max_area=max(max_area,area)
        # print(max_area)

# optimized 
        # height=[1,8,6,2,5,4,8,3,7]
        # i,j=0,len(height)-1
        # max_cap=0
        # while i<j:
        #     h=min(height[i],height[j])
        #     w=j-i
        #     area=h*w
        #     max_cap=max(max_cap,area)
        #     if height[i]<height[j]:
        #         i+=1
        #     else:
        #         j-=1
        # print(max_cap)
# -----------------------------------------------------------------------------------------
# majority element

# optimized
        # from collections import Counter
        # nums=[1,2,8,2,2,4,0,1,0]
        # hash_map=Counter(nums)
        # mx=0
        # maj=0
        # for val,cnt in hash_map.items():
        #     if cnt>mx:
        #         mx=cnt
        #         maj=val
        # print(maj)


# Brute Force 
        # nums=[1,2,8,2,2,4,0,1,0]
        # maj=0
        # mx_cnt=0
        # hash_set=set(nums)
        # for num in hash_set:
        #     cnt=nums.count(num)
        #     if cnt>mx_cnt:
        #         mx_cnt=cnt
        #         maj=num
        # print(maj)

# --------------------------------------------------------------------------------------------------------
#Reverse Vowels
#input-> s="hello"
#output-> "holle"

        # s="hello"
        # s=s.lower()
        # i=0
        # j=len(s)-1
        # s=list(s) # string is immutable that's why we convert it to list 
        # v="aeiou"
        # while i<j:
        #         if s[i] in v and s[j] in v:
        #                 s[i],s[j]=s[j],s[i]
        #                 i+=1
        #                 j-=1
        #         elif s[j] not in v:
        #                 j-=1
        #         else:
        #                 i+=1      
        # print("".join(s))

# ----------------------------------------------------------------------------------------
# check unique frequence   

        # nums=[1,1,2,1,5,5]
        # st=set(nums)
        # res=[]
        # for num in st:
        #         res.append(nums.count(num))
        # print(res)
        # print(len(res)==len(set(res)))

# ----------------------------------------------------------------------------------------------
#remove duplicates from unsorted array with tc=o(n) and sc=o(n)

        # nums=[13,1,3,1,1,9,0]
        # st=set()
        # for num in nums:
        #     if num not in st:
        #         st.add(num)
        # print(list(st))
# ----------------------------------------------------------------------------------------------
#remove duplicates from sorted array with TC=o(n) and sc=O(1) 

        # nums=[1,1,1,1,1,2,2,3,3,3,3]
        # i=0
        # for j in range(len(nums)):
        #     if nums[i]!=nums[j]:
        #         i+=1
        #         nums[i]=nums[j]
        # print(nums[:i+1])

# -----------------------------------------------------------------------------------------------
# sort even odd list

#SC=O(n)
        # nums=[1,4,3,6,8,11,15,8,9]
        # res=[]
        # for num in nums:
        # if num%2==0:
        #         res.append(num)
        # for num in nums:
        # if num%2!=0:
        #         res.append(num)
        # print(res)


#sc=O(1)
        # nums=[1,4,3,6,8,11,15,8,9]
        # n=len(nums)
        # i=0
        # while i<n:
        #     if nums[i]%2!=0:
        #         ele=nums.pop(i)
        #         nums.append(ele)
        #         n-=1
        #     else:
        #         i+=1
        # print(nums)

# ---------------------------------------------------------------------------------------------------
    
    
