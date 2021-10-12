cities = {
    'Lviv' : {
        'country' : 'ukraine',
        'population' : '721 000',
        'facts' : 'not in EU',
    },

    'Kiev': {
        'country' : 'ukraine',
        'population' : '2 817 000',
        'facts' : 'not in EU',
    },

    'Amsterdam' : {
        'country' : 'netherlands',
        'population' : '821 752',
        'facts' : 'in EU',
    }
}

for city_name, city_facts in cities.items():        #in this field we get name and facts from dictionary 'cities
    print(f"{city_name}:")                          #we print name of the city and drop facts down
    for names,facts in city_facts.items():          #we create 2 variable for names (country,population adn facts) add facts (ect.)
        print(f"\n\t{names} is {facts.title()}")
