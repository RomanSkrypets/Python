responds = {}
poolled_active = True

while poolled_active:
    name = input(f"What's your name? ")
    response = input("If you can visit olny one place in the world, which plase you will choose? ")

    responds[name] = response

    repeat = input("Do you wanna continue? y/n ")
    if repeat == 'n':
        poolled_active = False

print("---Pool Results---")
for name, response in responds.items():
    print(f"{name} want to visit {response}")

