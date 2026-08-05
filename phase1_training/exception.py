# a=int(input("enter:"))
# b=int(input("enter:"))
# try:
#     c=a/b
# except ZeroDivisionError:
#     print("can't divided by zero")
# else:
#     print(c)

# ---------------------------------------------------------------------------
 
# try:
#     a=int(input("enter:"))
#     b=int(input("enter:"))
#     c=a/b
# except ZeroDivisionError:
#     print("can't divided by zero")
# except ValueError:
#     print("Value raised")
# else:
#     print(c)

# ----------------------------------------------------------------------------

# a=int(input("enter:"))
# b=int(input("enter:"))
# try:
#     c=a/b
# except Exception as e:
#     print("Error",e)
# else:
#     print(c)

# -----------------------------------------------------------------------------

# a=int(input("enter:"))
# b=int(input("enter:"))
# try:
#     c=a/b
# except Exception as e:
#     print("Error",e)
# else:
#     print(c)
# finally:
#     print("completed")

# --------------------------------------------------------------------------
# again taking input when exception raised
# while True:
#     try:
#         a=int(input("enter:"))
#         b=int(input("enter:"))
#         c=a/b
#     except Exception as e:
#         print("Error",e)
#     else:
#         print(c)
#         break
#     finally:
#         print("completed")

# -----------------------------------------------------------------------------
# print(type(Exception))
# print(type(ValueError))
# ------------------------------------------------------------------------------
class TooYoung(Exception):
    def __init__(self,message):
        super().__init__(message)
def age_func(age):
    if age<18:
        raise TooYoungError("Too Young")
    else:
        print("Access Granted")
try:
    age_input=int
