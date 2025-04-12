current_users = ['Roman', 'admin', 'Oleg','Ivan', 'Bogdan', 'Stepan']
for users in current_users:
    if users == 'admin':
        print(f"Hello {users}, would you like to see a status report?")
    elif users:
        print(f"Welcome {users}, thank you for loggin again.")