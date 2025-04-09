def make_album(name,album):
    full_name = f"{name} {album}"
    return full_name.title()


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

