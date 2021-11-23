cinema = "Welcome! How old are you?\n"


while True:
    age = int(input(cinema))
    if age == "exit":
        break
    elif int(age) < int(3):
        print("Your ticket is free\t")
    elif int(age) >= int(3) and int(age) < int(12):
        print("Your ticket cost 10$\t")
    elif int(age) >= int(12):
        print("Your ticket cost 15$\t")
    
    