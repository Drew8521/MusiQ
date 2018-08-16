from models import Song
from random import choice

def random_song(genre):
    songs = choice(Song.query().filter(Song.genre==genre).fetch())
    random_song = {
        "title": songs.song,
        "album": songs.album,
        "artist": songs.artist,
        "genre": genre,
    }
    return random_song
