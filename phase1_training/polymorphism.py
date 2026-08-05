# operator overloading--(we want add 2 obj we use this)

# add dunder method

# class sem:
#     def __init__(self,sub1,sub2):
#         self.sub1=sub1
#         self.sub2=sub2
#     def __add__(self,other):
#         return(self.sub1+other.sub1,self.sub2+other.sub2)
    
# s1=sem(10,20)
# s2=sem(30,40)
# print(s1+s2)

# -------------------------------------------------------------------------------------------------------------
#sub dunder 
# class sem:
#     def __init__(self,sub1,sub2):
#         self.sub1=sub1
#         self.sub2=sub2
#     def __sub__(self,other):
#         return(self.sub1-other.sub1,self.sub2-other.sub2)
    
# s1=sem(10,20)
# s2=sem(30,40)
# print(s1-s2)
    
# -----------------------------------------------------------------------------------------------------------------
#repr - when we want to add more than 2 objects we use this

# class sem:
#     def __init__(self,sub1,sub2):
#         self.sub1=sub1
#         self.sub2=sub2
#     def __sub__(self,other):
#         return(self.sub1-other.sub1,self.sub2-other.sub2)
#     def __repr__(self):
#         return f"{self.sub1},{self.sub2}"
    
# s1=sem(10,20)
# s2=sem(30,40)
# print(s1)
# print(s2)
# s3=s1-s2
# print(s3)

# -------------------------------------------------------------------------------------------------------------------------

# method overloading (in 2 ways)

# 1)using default arguments
# class sum:
#     def add(self,a,b,c=0):
#         return a+b+c
# s=sum()
# print(s.add(1,2,3))

# 2) using positional arbitrary arguments
# class sum1:
#     def add(self,*args):
#         s1=0
#         for i in range(len(args)):
#             s1+=args[i]
#         return s1                    #return sum(args)   
# s=sum1()
# print(s.add(1,2,3))
# print(s.add(1,2,3,4,5))


# -------------------------------------------------------------------------------------------------------------------------------

# method Overriding

# class debit:
#     def pay(self):
#         print("Payment done using debit card")
# class Credit:
#     def pay(self):
#         print("Payment done using Credit card")
# class Upi:
#     def pay(self):
#         print("Payment done using Upi")
# def pay_method(pay_type):
#     pay_type.pay()
# d=debit()
# u=Upi()
# c=Credit()
# pay_method(d)
# pay_method(u)

# ------------------------------------------------------------------------