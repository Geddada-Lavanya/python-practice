# 1)Single Number
# nums=[8,2,6,2,8] ans=6 this is the single number 
# 2)Missing Number
# 3)Number of 1 bits
# 4)power of 2
# 5)reverse bits
# 6)subsets


# ------------------------------------------------------------------------------------------------------
# Single Number

        # arr=[8,4,6,4,8]
        # for num in arr:
        #     if arr.count(num)==1:
        #         print(num)
        #         break


        # arr=[8,4,6,4,8]
        # res=0
        # for num in arr:
        #     res^=num
        # print(res)


        # arr=[8,4,6,4,8]
        # from collections import Counter
        # cnt=Counter(arr)
        # for num,i in cnt.items():
        #     if i==1:
        #         print(num)

# ---------------------------------------------------------------------------------------------------

# 1 Single Number  XOR Basics
            # nums = [2,2,6,6,8]
            # res = 0
            # for n in nums:
            #     res ^= n
            # print(res)


# 2 Missing Number XOR + Range Numbers
            # nums = [1,2,4,0,5]
            # res = 0
            # for i in range(len(nums)):
            #     res ^= i^nums[i]
            # print(res^len(nums))




# 3 Number of 1 Bits (Hamming Weight)  Bit Counting
            # n = 5
            # count = 0
            # while n:
            #     count += n & 1
            #     n = n>>1
            # print(count)
    
# n=5
# print(bin(n).count('1'))




# 4 Power of Two
        # n = 24
        # print(True if n & (n-1) == 0 else False)


        # for i in range(32):
        #     ans = int(pow(2, i))
        #     if ans == n:
        #         return True
        # return False


# 5 Reverse Bits   Bit Shifting
        # n = 11
        # res = 0
        # for _ in range(32):
        #     res = res<<1
        #     res =   res | (n&1)
        #     n = n >> 1
        # print(bin(res),res)


        # n = 11
        # binary = bin(n)[2:]      # remove '0b'
        # binary = binary.zfill(32)  # make 32 bits
        # reversed_binary = binary[::-1]
        # ans = int(reversed_binary, 2)
        # print(ans)



# 6 Subsets (Power Set)    Bit Masking
        #     num = [1,2,3]
        #     n = len(num)
        #     res = []
        #     for mask in range(1<<n):
        #         sublist =[]
        #         for i in range(n):
        #             if (mask & 1) == 1:
        #                 sublist.append(num[i])
        #             mask >>= 1
        #         res.append(sublist)
        #     print(res)
# -----------------------------------------------------------------------------------
#Two SUM
        # arr=[7,24,6,2,11,15]
        # target=9
        # for i in range(len(arr)-1):
        #     for j in range(i+1,len(arr)):
        #         if arr[i]+arr[j]==target:
        #             print([i,j])


#using hashmap
        # arr=[1,2,3,4,7]
        # tar=9
        # dic={}
        # for i in range(len(arr)):
        #     if tar-arr[i] in dic:
        #         print([dic[tar-arr[i]],i])
        #     dic[arr[i]]=i
# -----------------------------------------------------------------------------------------------------------------------------
#contains Duplicates

        # arr=[1,2,3,1]
        # for num in arr:
        #     if arr.count(num)>1:
        #         print(True)
        #         break
        # else:
        #     print("False")


        # arr=[1,2,3,1]
        # arr_set=set(arr)
        # if len(arr_set)==len(arr):
        #     print("False")
        # else:
        #     print("True")
# ------------------------------------------------------------------------------------------------------------------------------
# product of array except itself

        # arr=[1,2,3,4]
        # prod=1
        # for i in range(len(arr)):
        #     prod*=arr[i]
        # for i in range(len(arr)):
        #     arr[i]=prod//arr[i]
        # print(arr)


        # def productExceptSelf(nums):
        #         res = []
        #         for i in range(len(nums)):
        #                 prod = 1
        #                 j = 0
        #                 while j < len(nums):
        #                         if j != i:
        #                                 prod *= nums[j]
        #                         j += 1
        #                 res.append(prod)
        #         return res
        # nums = [1,2,3,4]
        # print(productExceptSelf(nums))
# ---------------------------------------------------------------------------------------------
# nums=[1,4,2,2,1,1,3,1,1]
# 1)most repeated element(using hashing)

        # dic={}
        # nums=[1,2,3,1,1,4,2,1,1]
        # for i in nums:
        #         dic[i]=dic.get(i,0)+1
        # mx=0
        # mx_val=0
        # for val,cnt in dic.items():
        #     if cnt>mx:
        #         mx=cnt
        #         mx_val=val
        # print(mx_val)


        # dic={}
        # nums=[1,2,3,1,1,4,2,1,1]
        # for i in nums:
        #         dic[i]=dic.get(i,0)+1
        # print(max(dic, key=dic.get))

# -------------------------------------------------------------------------------
#count digits in a number

        # n=12345
        # cnt=0
        # while n:
        #     digit=n%10
        #     cnt+=1
        #     n//=10
        # print(cnt)


        # st=str(n)
        # cnt=0
        # for i in st:
        #     cnt+=1
        # print(cnt)
# -----------------------------------------------------------------------------------------
#reverse a number

        # n=12345
        # st=str(n)
        # print(int(st[::-1]))


        # n=12345
        # res=0
        # while n:
        #     digit=n%10
        #     res=res*10+digit
        #     n//=10
        # print(res)
# --------------------------------------------------------------------------------------------
#check palindrome number

        # n=12353521
        # temp=n
        # res=0
        # while n>0:
        #         digit=n%10
        #         res=res*10+digit
        #         n//=10
        # print(res==temp)


        # n=123621
        # st=str(n)
        # print(st==st[::-1])
# ------------------------------------------------------------------------------------------------