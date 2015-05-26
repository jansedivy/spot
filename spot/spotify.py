from apple_script import AppleScript


class Spotify():
    def run_command(self, command):
        return AppleScript.run('''
        if appIsRunning("Spotify") then
            tell application "Spotify"
                {}
            end tell
        end if

        on appIsRunning(appName)
            tell application "System Events" to (name of processes) contains appName
        end appIsRunning
        '''.format(command))

    def pause(self):
        return self.run_command('pause')

    def start(self):
        return self.run_command('play')

    def toggle(self):
        return self.run_command('playpause')

    def next_track(self):
        return self.run_command('next track')

    def previous_track(self):
        return self.run_command('previous track')

    def play_song(self, song):
        return self.run_command('play track "spotify:track:{}"'.format(song.track_id))

    def play_song_from_playlist(self, song, playlist):
        return self.run_command('play track "spotify:track:{}" in context "spotify:user:{}:playlist:{}"'.format(song.track_id, playlist.user_id, playlist.playlist_id))

    @property
    def current_track(self):
        return self.run_command('''
            if (player state = playing) then
                set trackName to name of current track
                set artistName to artist of current track
                return trackName & " / " & artistName
            end if
        ''')
