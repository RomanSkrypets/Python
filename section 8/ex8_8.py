def make_album(name_artist, album, songs=None):
    full_name={'artist': name_artist,
               'album': album}
    if songs:
        full_name['songs'] = songs
    return full_name

while True:
    print("\nWrite artist name below")
    print("\nPrint 'q' to quite")

    name = input("Write artist name: ")
    if name == 'q':
        break

    album = input("Write album: ")
    if album == 'q':
        break

    songs = input("Write count of songs: ")

    formatted_artist = make_album(name, album, songs)
    print(formatted_artist)