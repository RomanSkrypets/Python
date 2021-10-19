pizza = "\nPlease, add your ingridients in pizza"
pizza += "\nYour ingridiance:"

ingr = True
while ingr:
    ingridiance = input(pizza)

    if ingridiance == 'quit':
        break;
    else:
        print(f"{ingridiance.title()} add to pizza")