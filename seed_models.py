from models import Song
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def seed_data():
    client_credentials_manager = SpotifyClientCredentials(
        client_id='a557faea8f66459eb23e1ae3d46dcd0a',
        client_secret='07598c693dc740eba6821d22923f0f60',
        proxies=None)
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.user_playlist('Spotify', '37i9dQZF1DX1N5uK98ms5p')
    for result in results:
        track = Song(title=results['tracks']['items']['name']).put()
