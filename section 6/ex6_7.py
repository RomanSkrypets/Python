people = {

            'oleg' : {  'first_name' : "Oleg",
                        'last_name' : "Levytskyi",
                        'age' : '24',
                        'city' : "Stryi",

            },

            'stepan' : {
                'first_name' : 'Stepan',
                'last_name' : 'Ganusiak',
                'age' : '23',
                'city' : 'Kiev'
            },

            'lubko' : {
                'first_name' : 'Lubomyr',
                'last_name' : 'Yarych',
                'age' : '22',
                'city' : 'Lviv'
            },
}

for user_name, user_info in people.items():
    print(f"\nUsername: {user_name}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    age = f"{user_info['age']}"
    city = f"{user_info['city']}"

    print(f"Hello {full_name},\nyour age: {age}, \nand you live in {city} city.")
