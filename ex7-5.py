cinema = "Welcome! How old are you?\n"


while True:
    age = int(input(cinema))
    if age == "exit":
        break
    elif age < str(3):
        print("Your ticket is free")
    elif age >= str(3) and age < str(12):
        print("Your ticket cost 10$")
    elif age > str(12):
        print("Your ticket cost 15$")
    
    