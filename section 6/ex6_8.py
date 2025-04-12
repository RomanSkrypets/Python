animal_0 = {
    'animal' : 'cat',
    'owner' : 'Roman'
}

animal_1 = {
    'animal' : 'dog',
    'owner' : 'Stepan'
}

animal_2 = {
    'animal' : 'cat',
    'owner' : 'Oleg'
}

pets = [animal_0, animal_1, animal_2]

for pet in pets:
    print(f"{pet['owner']} has a {pet['animal']}")