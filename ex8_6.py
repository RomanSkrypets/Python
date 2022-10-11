def city_country(name, country):
    num = f"{name}, {country}"
    return num.title()

cou = city_country('Lviv','Ukraine')
print(cou)
cou = city_country('New York','USA')
print(cou)
cou = city_country(country="England", name="London")
print(cou)
