# lst=[1,2,3,1,3,1]
# # print(type(lst))
# # lst.pop(3)
# # lst.remove(3)
# res=sorted(lst)
# print(res)
# print(lst)
# -------------------------------------------------------------------
# lst=[1,2,3,1,3,1]
# lst.sort()
# print(lst)
# -----------------------------------------------------------------------
# lst=[1,"r",3,5]
# res=lst.sort(key=str)
# print(res)
# ---------------------------------------------------------------------------
#Creating List and taking Input values
# 1)
# lst=list()
# print(type(lst))
# print(lst)

# 2)
# lst=input().split() #for str input values
# or
# lst=list(map(str,input().split()))
# print(lst)

# 3)
# lst=[]
# for i in range(5):
#     item=input()
#     lst.append(int(item))

# 4)
# lst=list(map(int,input().split()))
# print(lst)

# -------------------------------------------------------------------------
#infinite loop

# lst=[] 
# while True:
#     item=input()
#     if item.lower()=="stop":
#         break
#     lst.append(item)
# print(lst)

# ---------------------------------------------------------------------------

#list Comprehnsion
# lst=[int(i) for i in input("enter").split()]
# lst1=[i for i in lst if i%2==0]
# print(lst)
# print(lst1)

# ---------------------------------------------------------------------------------
#set comprehnsion
# lst=set([int(i) for i in input("enter").split()])
# lst1=set([i for i in lst if i%2==0])
# print(lst)
# print(lst1)
# --------------------------------------------------------------------------------
# lst=[int(i) for i in input("enter").split()]
# set1={x**2 for x in lst if x>0 and x%2==0}
# print(set1)
# ----------------------------------------------------------------------------


# for each loop
# sorted()
# reversed()
# nested lists
# updating an elemnt using index
