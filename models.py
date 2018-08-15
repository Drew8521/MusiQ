

from google.appengine.ext import ndb

class Song(ndb.Model):
    genre = ndb.StringProperty(required=True)
    song = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)
    album = ndb.StringProperty(required=True)
    url = ndb.StringProperty(required=True)
