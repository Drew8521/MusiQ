

from google.appengine.ext import ndb

class Song(ndb.Model):
    title = ndb.StringProperty(required=True)
    album = ndb.StringProperty(required=True)
    artist = ndb.StringProperty(required=True)
    
