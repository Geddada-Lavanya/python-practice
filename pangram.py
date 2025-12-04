s=input()
a="abcdefghijklmnopqrstuvwxyz"
s1=("".join(s)).lower()
s1=list(s1)
for i in a:
    if i not in s1:
        print("not pangram")
        break
else:
    print("pangram")
    