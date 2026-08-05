# tup=()
# tup1=tuple()
# tup=tuple(input().split())
# tup=tuple(map(int,input().split()))
# print(tup)

# ---------------------------------------------------------------------------------------

# lst_tup=[]
# for _ in range(5):
#     item=input()
#     lst_tup.append(item)
# tup=tuple(lst_tup)
# print(tup)

# -----------------------------------------------------------------------------------------

# lst=[]
# while True:
#     item=input()
#     if item.lower()== "stop":
#         break
#     lst.append(item)
# tup1=tuple(lst)
# print(tup1)

# ----------------------------------------------------------------------------------------------
# reversed() function vs reverse() function

# lst=[1,3,2,4]
# lst.reverse()
# print(lst)
# print(reversed(lst))
# temp=reversed(lst)
# print(tuple(temp)) # without converting to tuple we not get

# ----------------------------------------------------------------------------------------------
# PACKING AND UNPACKING


# tup=((1,2,3),(4,5,6),(7,8))
# lst=list(tup)
# lst1=[]
# for i in range(len(lst)):
#     a=lst[i]
#     a=a[::-1]
#     a=tuple(a)
#     lst1.append(a)
# print(tuple(lst1))

# ---------------------or------------------------------

# tup=((1,2,3),(4,5,6),(7,8))
# temp1=tuple(reversed(tup[0]))
# temp2=tuple(reversed(tup[1]))
# temp3=tuple(reversed(tup[2]))
# rev_tup=(temp1,temp2,temp3)
# print(rev_tup)

# ------------------------------------------------------------------------------------------------
