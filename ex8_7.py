def make_album(name,album,songs=None):
    full_name = {'name': name, 'album': album}
    if songs:
        full_name['songs'] = songs
    return full_name

# add ex
'''
while True:
    print("\nPlease tell me mucitians name and album:")
    print("('Enter q for exit')")
    f_name = input("Name: ")
    if f_name == "q":
        break

        
    f_album = input("Album name: ")
    if f_album == "q":
        break
    
    formatted_name = make_album(f_name, f_album)
    formatted_name
    print(f"\nHello, {formatted_name}")
'''


c = make_album('slayer','raining blood', 6)
print(c)
c = make_album('metallica','fuel', None)
print(c)
c = make_album('1914','cry', songs=7)
print(c)

