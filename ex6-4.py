#ex6-4
""""
prog_lan = {
    "keys" : "value",
    "sorted" : "abc",
    "set" : "unical",
    "for" : "loop",
    "input" : "text input"
}

for key, value in prog_lan.items():
    print(f"The dictionary keys is: {key} \nand values: {value}")
"""
#ex6-5
"""
big_river = {
    "nile" : "egypt",
    "dnipro" : "ukraine",
    "misissipi" : "usa",
}

for river, country in big_river.items():
    print(f"The {river.title()} runs through {country.title()}")
"""
#ex6-6

favourive_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    'roman' : 'python',
    'oleg' : 'security',
}

for people, lang in favourive_languages.items():
    print(f"Hello {people.title()} thank you for the choise language {lang.title()}")

if 'olga' not in favourive_languages.keys():
    print(f"Sorry Olga you don't have a choise")