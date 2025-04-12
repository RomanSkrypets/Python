big_river = {
    "nile" : "egypt",
    "dnipro" : "ukraine",
    "misissipi" : "usa",
}

for river, country in big_river.items():
    if country == 'usa':
        print(f"The {river.title()} runs through {country.upper()}")
    else:
        print(f"The {river.title()} runs through {country.title()}")
    