# 1) sum of digits until becomes single digit

        # def sum_upto_single(n):
        #     sm=0
        #     while n>0:
        #         digit=n%10
        #         sm+=digit
        #         n=n//10
        #     return sum_upto_single(sm) if sm>9 else sm
        # n=int(input())
        # print(sum_upto_single(n))
# --------------------------------------------------------------------------------------------
# 2)ques= print largest num and word 
# # my approach 

        # s=input()
        # alp=""
        # num=""
        # max_alp=""
        # max_num=""
        # for i in s:
        #     if i.isdigit():
        #         num+=i
        #         if alp>max_alp:
        #             max_alp=alp
        #             alp=""
        #     elif i.isalpha():
        #         alp+=i
        #         if num>max_num:
        #             max_num=num
        #             num=""
        # if s[-1].isdigit():
        #     max_num=num
        # elif s[-1].isalpha():
        #     max_alp=alp
        # print(max_num+max_alp)


# #sir approach

        # s=input()
        # res=[0,""]
        # i=0
        # while i<len(s):
        #     num=""
        #     alp=""
        #     while s[i].isdigit():
        #         num+=s[i]
        #         i+=1
        #     while i<len(s) and s[i].isalpha():
        #         alp+=s[i]
        #         i+=1
        #     res[0]=res[0] if res[0]>int(num) else int(num)
        #     res[1]=res[1] if len(res[1])>len(alp) else alp
        # print(res)
# ----------------------------------------------------------------------------------------------
# Happy Number

# mine approach
        # def happy_num(num,res=[]):
        #     if num==1:
        #         return "Happy Number"
        #     elif num in res:
        #         return "not a happy number"
        #     res.append(num)
        #     sm=0
        #     while num>0:
        #         digit=num%10
        #         sm=digit**2
        #         num=num//10
        #     return happy_num(sm,res) 
        # n=int(input())
        # print(happy_num(n))

#sir approach

        # n=4
        # seen=set()
        # while n!=1 and n not in seen:
        #     seen.add(n)
        #     temp=0
        #     for i in str(n):
        #         temp+=int(i)**2
        #     n=temp
        # if n==1:
        #     print("Happy Number")
        # else:
        #     print("not a happy number")

# --------------------------------------------------------------------------------------------------------------------
# if "123":
#     print("h")  

# if "":
#     print("h") 