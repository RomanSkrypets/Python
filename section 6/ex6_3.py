list = {
    'Integer' : 1,
    'String' : 'blabla',
    'Boolean' : 'true',
    'List' : "list_example",
    'Tuple' : "same_thing",
}

for names, value in list.items():
    print(f"There was last article {names.title()}\n \t\t\tand value: {value}")