# num=int(input())

# if(num>0):
#     if (num < 10):
#         if(num%2==0):
#             print("num is +ve and single digit and even")
#         else:
#             print("number is +ve and single digit and odd")
#     else:
#         if(num%2==0):
#             print("num is +ve and not a single digit and even")
#         else:
#             print("num is +ve and not a single digit and odd")
# elif(num<0):
#     if (num > -10):
#         if(num%2==0):
#             print("num is -ve and single digit and even")
#         else:
#             print("num is -ve and single digit and odd")
#     else:
#         if(num%2==0):
#             print("num is -ve and not a single digit and even")
#         else:
#             print("num is -ve but not a single digit and odd")
# else:
#     print("num is zero")



# -------------------------------------------------------------------------------


num=int(input("enter a number: "))
if(num>0):
    if(num<10):
        res="Number is single-digit positive number"
    elif(num<100):
        res="Number is double digit positive number"
    else:
        res="number is large positive number"
elif(num<0):
    if(num>-10):
        res="Number is single-digit negative number"
    elif(num<=-10):
        res="Number is double-digit negative number"
    else:
        res="number is large negative number"
else:
    res="Number is zero"

if(num!=0):
    if(num%2==0):
        res+=" and it is even"
    else:
        res+=" and it is odd"

    print(res)











marks=int(input("Enter marks: "))

if marks<0 or marks>100:
    print("Invalid input! Marks should be between 1 and 100")
else:
    if(marks==100):
        print("Perfect Score! Outstanding performance!")
    elif(marks>=90):
        print("Grade A,Excellent!")
    elif(marks>=75):
        print("Grade B,Very Good!")
    elif(marks>=60):
        print("Grade C,Good!")
    elif(marks>=40):
        print("Grade D,Needs Improvement!")
    else:
        print("Grade F,Fail")
        print("Better luck next time")