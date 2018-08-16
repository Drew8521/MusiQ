from models import Song
from random import choice

def random_song(genre):
    results = Song.query().filter(Song.genre==genre).fetch()
    print("HELLO")
    print(results)
    songs = choice(results)
    random_song = {
        "title": songs.song,
        "album": songs.album,
        "artist": songs.artist,
        "genre": genre,
    }
    return random_song
