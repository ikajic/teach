# open the file with the music data in the read-only mode
f = open('ivana_music.txt', 'r')

# dictionary that will contain artist and album names
music_collection = {}

# fill the dictionary with the data from the file
for line in f.readlines():
    pos_separator = line.find(':')
    artist = line[0:pos_separator]
    album = line[pos_separator+2:]
    album = album.replace('\n', '')

    if artist not in music_collection:
        music_collection[artist] = []

    music_collection[artist].append(album)

# answer user's questions
nr_artists = len(music_collection.keys())
nr_albums = len(music_collection.values())

print 'Ivana has', nr_artists, 'artists and ', nr_albums, \
      'albums in her collection'

# find out which artist has the most albums
most_albums_artist_name = ''
max_albums = 0

for artist in music_collection.keys():
    albums = music_collection[artist]
    nr_albums_this_artist = len(albums)

    if nr_albums_this_artist > max_albums:
        max_albums = nr_albums_this_artist
        most_albums_artist_name = artist

print 'Artist with most albums is', most_albums_artist_name, '(', max_albums,\
      'albums )'
