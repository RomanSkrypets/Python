current_users = []

if current_users:   
    for users in current_users:
        if users == 'admin':
            print(f"Hello {users}, would you like to see a status report?")
        elif users:
            print(f"Welcome {users}, thank you for loggin again.")
else:
    print(f"We need to find some users!")