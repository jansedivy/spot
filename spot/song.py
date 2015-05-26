class Song():
    def __init__(self, title, artist, track_id):
        self.title = title
        self.artist = artist
        self.track_id = track_id

    @property
    def full_title(self):
        return '{} / {}'.format(self.title, self.artist)
