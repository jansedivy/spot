from urllib.request import urlopen
import json
import re
import os

from playlist import Playlist
from song import Song


class Manager():
    # TODO: Find better way to download playlist data. Some random website with
    # spotify json is not very useful
    PLAYLIST_URL = 'http://tomashenden.com/projects/spotify-php-playlist.php?uri=spotify:user:{}:playlist:{}&output=json'

    CACHE_DIR = 'playlists'

    @staticmethod
    def get_cache_path_for(playlist_id):
        return os.path.join(Manager.CACHE_DIR, '{}.json'.format(playlist_id))

    @staticmethod
    def download_playlist(user_id, playlist_id):
        # TODO: Load playlists from spotify app. Take a look at libspotify
        data = urlopen(Manager.PLAYLIST_URL.format(user_id, playlist_id)).read()
        with open(Manager.get_cache_path_for(playlist_id), 'w') as f:
            parsed = json.loads(data.decode('utf-8'))
            parsed['user_id'] = user_id
            parsed['playlist_id'] = playlist_id
            f.write(json.dumps(parsed))

    @staticmethod
    def load_playlist(user_id, playlist_id):
        path = Manager.get_cache_path_for(playlist_id)
        if not os.path.exists(path):
            Manager.download_playlist(user_id=user_id, playlist_id=playlist_id)

        with open(path, 'r') as f:
            data = json.loads(f.read())

            playlist = Playlist(data['name'], user_id=user_id, playlist_id=playlist_id)
            for track in data['tracks']:
                track_id = re.findall('/(\w+)$', track['link'])[0]
                playlist.add_song(Song(track['title'].strip(), track['artist'].strip(), track_id))

            return playlist
