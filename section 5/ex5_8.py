current_users = ['Roman', 'admin', 'Oleg','Ivan', 'Bogdan', 'Stepan']
cur = current_users.copy()
cur = ['roman', 'Admin','oleg','ivan','bogdan','stepan']
#users = []   #for empty list 
new_users = ['Galyna', 'Iruna','Artem','Andrew','Ivan','Olga']
for new in new_users:
    if new in current_users:
        print(f"{new} you must rename profile")
    else:
        print(f"Welcome {new}")