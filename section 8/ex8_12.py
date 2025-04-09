def ingridients(*toppings):
    print("Add ingridients: ")
    for topping in toppings:
        print(f"- {topping}")

ingridients('cheese', 'meat')
ingridients('bread')
ingridients('seed')