# num1=int(input("enter 1st value:"))
# num2=int(input("enter 2nd value:"))

# operator=input("enter operator: ")

num1,num2,operator=input().split(",")
num1=int(num1)  
num2=int(num2)

if(operator=="+"):
    print(f"addition={num1+num2}")
elif(operator=="-"):
    print(f"subtraction:{num1-num2}")
elif operator=="*":
    print(f"multiplication={num1*num2}")

# elif operator=="/" and b!=0 :
#     print(f"division:{num1/num2}")

elif operator=="/":
    if num2==0:
        print("num2 value must be greater than 0 ,Enter another value:")
        num2=int(input())
    else:
        print(f"division:{num1/num2}")
else:
    print("Invalid Operator")