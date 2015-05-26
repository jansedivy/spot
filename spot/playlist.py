class Playlist():
    def __init__(self, name, user_id, playlist_id):
        self.name = name
        self.user_id = user_id
        self.playlist_id = playlist_id
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_songs(self):
        for song in self.songs:
            print(song.full_title)

    def find(self, name):
        for song in self.songs:
            if song.full_title == name:
                return song
