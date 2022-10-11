
numbers = {
    'Roman' : [15,16,36,34,77],
    'Oleg' : [32,87,45,34,66],
    'Stepan' : [87,43,123,64,32],
    'Igor' : [55,574,876,5,43],
    'Lubko' : [300,745,53,33,21],
}

for people, num in numbers.items():
    print(f"{people} has a number:")
    for numb in num:
        print(f"\t\t\t{numb}")