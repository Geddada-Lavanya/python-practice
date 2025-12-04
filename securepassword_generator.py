import random
num=[0,1,2,3,4,5,6,7,8,9]
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Symbols=['!','@','$','%','^','#','&','+','-','*','(',')']
print("SET YOUR PASSWORD:")
password=[] #list is taken to use shuffle function in line 19
nums_chosen=int(input("How many numbers do you want in your password?"))
for i in range(1,nums_chosen+1):
 char=random.choice(num)
 password+= str(char)#to change the numbers into strings as they are not coverted intially
letters_chosen=int(input("How many letters do you want in your password?"))
for i in range(1,letters_chosen+1):
 char=random.choice(letters)
 password += char
symbols_chosen=int(input("How many symbols do you want in your password?"))
for i in range(1,symbols_chosen+1):
 char=random.choice(Symbols)
 password += char
random.shuffle(password)
password="".join(password) #join() function is string method,used to concatenate elements of an iterable (such as a list, tuple, or any sequence) into a single string, with a specified separator between the elements.
print(password)