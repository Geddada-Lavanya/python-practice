whether=input("enter:")
time_of_day=input()
if whether=="sunny":
    if time_of_day=="night":
        print("sleep")
    else:
        print("play cricket")
elif whether=="rainy":
    if time_of_day=="day":
        print("play video games")
    else:
        print("sleep")
else:
    print("play indoor games")

