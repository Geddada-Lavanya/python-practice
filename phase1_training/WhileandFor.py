# sum of n natural numbers using while Loop 

# n=int(input())
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

# ------------------------------------------------------------------------------
#break

# n=int(input())
# i=1
# sum=0
# while i<=n:
#     if i==5:
#         break
#     sum+=i
#     i+=1
# print(sum)

# ----------------------------------------------------------------------------------

# for i in range(10):
#     if(i==5):
#         continue
#     print(i)

# -------------------------------------------------------------------------------
#continue 

# n=int(input())
# i=1
# sum=0
# while i<=n:
#     if i==5:
#         continue
#     sum+=i
#     i+=1
# print(sum)

# -----------------------------------------------------------------------------------
# fizzbuzz
#question--- when it is a negative number then it again asks to another value ,we want to give the inputs continuously then we use
# while True:

# while True:
#     n=int(input())
#     if(n==0):
#         break
#     if(n<0):
#         print("Enter another value:")
#         continue
#     if(n%2==0 and n%3==0):
#         print("FizzBuzz")
#     elif(n%2==0):
#         print("Fizz")
#     elif(n%3==0):
#         print("Buzz")
#     else:
#         print("other")

# --------------------------------------------------------------------------------------

# n=int(input())
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n)
#     else:
#         print("*"+" "*(n-2)+"*")

# ----------or--------------------

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#--------------------------------------------------------------------------------------------

#floyd's Traingle

# n=int(input())
# val=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(val,end=" ")
#         val+=1
#     print()

# --------------------------------------------------------------------------------------------
# 10
# 10 20
# 10 20 30

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j*10,end=" ")
#     print()

# --------------------------------------------------------------------------------------------
# a
# a e 
# a e c
# a e c d
# a e c d e

# lst=['a','e','c','d','e']
# lst=list(map(str,input().split()))
# for i in range(1,len(lst)+1):
#     for j in range(i):
#         print(lst[j],end=" ")
#     print()

# -----------------------------------------------------------------------------------------------
 