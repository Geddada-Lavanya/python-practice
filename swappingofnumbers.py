a=int(input("enter a value:"))
b=int(input("enter b value:"))

#with using temporary variable
temp=a
a=b
b=temp

#without using temporary variable
a=a+b
b=a-b
a=a-b

print(f"value of a is:{a}")
print(f"value of b is:{b}")



