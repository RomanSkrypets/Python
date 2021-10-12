age = input("Your age: ")
if int(age) < 2:
    print('You baby')
elif int(age) >= 2 and int(age) < 4:
    print('You maluk')
elif int(age) >= 4 and int(age) < 13:
    print("You adult")
elif int(age) >= 13 and int(age) < 20:
    print("You pidlitok")
elif int(age) >= 20 and int(age) < 65:
    print("You people")
elif int(age) >= 65:
    print("You are old")