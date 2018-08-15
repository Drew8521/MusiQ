#main.py
#the import section
import webapp2
import jinja2
import os
import pprint
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from google.appengine.ext import ndb

from models import Song
from seed_models import seed_data

#from google.cloud import datastore

# from requests_toolbelt.adapters import appengine
# appengine.monkeypatch()

import requests
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/title.html')
        self.response.write(template.render())

class Profile(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/profile.html')
        self.response.write(template.render())

class GenreChooser(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/genre_chooser.html')
        self.response.write(template.render())

class DifficultyChooser(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/difficulty_chooser.html')
        self.response.write(template.render())

class Hello(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/hello.html')

        client_credentials_manager = SpotifyClientCredentials(
            client_id='a557faea8f66459eb23e1ae3d46dcd0a',
            client_secret='07598c693dc740eba6821d22923f0f60',
            proxies=None)
        client_credentials_manager = SpotifyClientCredentials()


class Playlist(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/playlist.html')
        client_credentials_manager = SpotifyClientCredentials(
            client_id='a557faea8f66459eb23e1ae3d46dcd0a',
            client_secret='07598c693dc740eba6821d22923f0f60',
            proxies=None)
        client_credentials_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        results = sp.user_playlist('Spotify', '37i9dQZF1DX1N5uK98ms5p')
        #print json.dumps(results, indent=4)
        self.response.write(template.render({"playlist": results['tracks']['items']}))


class Greeting(ndb.Model):
    """Models an individual Guestbook entry with content and date."""
    content = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_book(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-cls.date)


class Datastore(ndb.Model):
    def get(self):
        client_credentials_manager = SpotifyClientCredentials(
            client_id='a557faea8f66459eb23e1ae3d46dcd0a',
            client_secret='07598c693dc740eba6821d22923f0f60',
            proxies=None)
        client_credentials_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        results = sp.user_playlist('Spotify', '37i9dQZF1DX1N5uK98ms5p')
          # We set the parent key on each 'Greeting' to ensure each guestbook's
        # greetings are in the same entity group.


        guestbook_name = 'artist'
        greeting = Greeting(parent=ndb.Key("Book",
                                          guestbook_name or "*notitle*"),
                            content= 'song')
        greeting.put()

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        selfs.response.write('Seed Data Added ')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/datastore', Datastore),
    ('/hello', Hello),
    ('/profile', Profile),
    ('/playlist', Playlist),
    ('/genre-chooser', GenreChooser),
    ('/difficulty-chooser', DifficultyChooser)
    ('/seed-models', LoadDataHandler)
], debug=True)
