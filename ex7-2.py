person = int(input("How people you want reserved? "))


if person > 8:
    print(f"If you have {person} persons - you must wait")
else:
    print("Your table is reserved")