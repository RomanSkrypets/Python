cinema = "Welcome! How old are you?\n"

active = True
while active:
    age = input(cinema)
    if age == "quit":
        break
    elif age < str(3):
        print("Your ticket is free")
    elif age >= str(3) and age < str(12):
        print("Your ticket cost 10$")
    elif age > str(12):
        print("Your ticket cost 15$")
    
    