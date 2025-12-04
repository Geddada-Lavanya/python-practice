m=int(input("enter maths marks:"))
p=int(input("enter physics marks:"))
e=int(input("enter english marks:"))

total_marks=m+p+e
average=(total_marks)/3
percentage=(total_marks/300)*100

grade=""
if percentage>90:
    grade="A"
elif percentage>80 and percentage<=90:
    grade="B"
else :
    grade="p"

print(f"Total marks:{total_marks} \nAverage:{average} \nPercentage:{percentage} \ngrade={grade}")

