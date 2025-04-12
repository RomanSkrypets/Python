current_users = ['Roman', 'admin', 'Oleg','Ivan', 'Bogdan', 'Stepan']

new_users = ['Roman', 'Petro','Oleg','John','Yaryna','Igor']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new in new_users:
    if new.lower() not in current_users_lower:
        print(f"Welcome {new.title()}")
    else:
        print(f"{new} name already exist, please rename your user")