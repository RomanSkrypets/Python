def make_album(name_artist, album, songs=None):
    full_name={'artist': name_artist,
               'album': album}
    if songs:
        full_name['songs'] = songs
    return full_name

musician = make_album('Rammstein', 'sehnsucht')
print(musician)
musician = make_album('ACDC', 'Back in black', songs=23)
print(musician)
musician = make_album('Metallica', 'ride the lightning')
print(musician)
