

from google.appengine.ext import ndb

class Song(ndb.Model):
    genre = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)
    album = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required=True)
