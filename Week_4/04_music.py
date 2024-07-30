class Artist():

    def __init__(self, name):
        self.artist_name = name
        self.albums_list = []

    def add_album(self, album_name, tracklist=[]):
        # album_name, artist, tracklist=[]
        new_album = Album(album_name, self, tracklist)
        self.albums_list.append(new_album)

    def print_catalog(self):
        for album in self.albums_list:
            print(f"Album name: {album.album_name}")
            for track in album.tracklist:
                print(
                    f'Track number:{track.track_number}, Track name: {track.track_name}')

    def artist_summary(self):
        for album in self.albums_list:
            album_duration = 0
            for track in album.tracklist:
                album_duration += track.track_duration
                # print(f'Album')


class Album():

    def __init__(self, album_name, artist, tracklist=[]):
        self.album_name = album_name
        self.artist = artist
        self.tracklist = tracklist

    def add_track(self, track_number, track_name, track_duration):
        # track_number, track_name, track_duration
        new_track = Track(track_number, track_name, track_duration)
        self.tracklist.append(new_track)


class Track():

    def __init__(self, track_number, track_name, track_duration):
        self.track_number = track_number
        self.track_name = track_name
        self.track_duration = track_duration


a1 = Artist("Adele")
a1.add_album('25', [Track(1, "Hello", 200), Track(
    2, "I like it", 300), Track(3, "some like it hot", 400)])
a1.albums_list[0].add_track(4, 'I love you', 500)
# a2 = Artist("beyonce")
a1.add_album('21', [Track(1, "Goodbye", 200)])

a1.print_catalog()
a1.artist_summary()
print('end of file')
