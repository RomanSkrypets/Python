favourite_places = {
    'roman' : ['river','mountain','lviv'],
    'stepan' : ['kiev','train','lexemburg'],
    'oleg' : ['sea', 'island','beach'],
}

for people,place in favourite_places.items():
    print(f"{people.title()} like places: ")
    for places in place:
        print(f"\t\t{places.title()}")