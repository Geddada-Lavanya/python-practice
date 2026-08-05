# Type function
# str="Pragati"
# print(str[::-1])
# print(str[::2])

# str=input()
# print(str[::2])
# print(str[-1::-2])
# print(str[:len(str):2])
# print(len(str))
# print(str.lower())
# print(str.upper())
# print(str[::-1])
# print(str[::])
# print(str.capitalize())
# print(str.title())
# print(str.swapcase())
# print(str.startswith('a'))
# print(str.endswith("nya"))
# print(str.index('a'))
# print(str.find('a'))

# print(str.index('c'))
# print(str.find('c'))

# print(str.find("a",2))  # it won't work when we take input dynamically
# for that we have write like below
# str=input()
# temp=str.find("a")
# print(str.find("r",temp+1))



# str="lavanya     "
# print(str[7])
# str="    lavanya"
# print(str[5])


# str="  hello  "
# print(str)
# print(str.strip())
# print(str)
# print(str.lstrip())
# print(str)

# str="kavya"
# print(len(str))
# str1="    kavya"
# print(len(str1))
# str2=input()
# print(len(str2))


# str="pragatiTengg"
# a,b,c=str.split("a")
# print(a,b,c)
# d,e=str.split("T")
# print(d,e)

# a,b=input().split()
# print(b[::2])

# print("test".ljust(10,"*"),"20","30")
# print("test".rjust(10,"*")+"20","30")
# str="test"
# print(str.ljust(8,"&"))
# print(str.rjust(8,"&"))
# print(str.center(8,"&"))
# print(str.rjust(8))

num="-42"
print(num.rjust(5,"0"))
print(num.zfill(5))