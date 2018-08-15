from models import Song
from random import choice

def random_pop_song():
    songs = choice(Song.query().filter(Song.genre=="Pop").fetch())
    random_list = {
        "title": songs.song,
        "album": songs.album,
        "artist": songs.artist,
    }
    return random_list
