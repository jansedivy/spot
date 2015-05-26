import argparse

from spotify import Spotify
from playlist import Playlist
from manager import Manager


def main():
    # TODO(sedivy): Store user_id in a config file
    user_id = '11124246152'
    playlist_id = '3dDVf6yzpX5IQK2R7GtYcq'

    playlist = Manager.load_playlist(user_id=user_id, playlist_id=playlist_id)

    parser = argparse.ArgumentParser(description='Spotify command line')
    parser.add_argument('command', metavar='command', nargs='+', help='Command')

    args = parser.parse_args()

    command = args.command[0]
    arguments = ' '.join(args.command[1:])

    spotify = Spotify()

    if command == 'list':
        playlist.print_songs()
    elif command == 'play':
        spotify.play_song_from_playlist(playlist.find(arguments), playlist)
    elif command == 'pause':
        spotify.pause()
    elif command == 'start':
        spotify.start()
    elif command == 'toggle':
        spotify.toggle()
    elif command == 'next_track':
        spotify.next_track()
    elif command == 'previous_track':
        spotify.previous_track()
    elif command == 'play_song':
        spotify.play_song(arguments)
    else:
        print('Undefined command "{}"'.format(command))

if __name__ == '__main__':
    main()
