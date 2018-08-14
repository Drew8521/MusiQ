from google.appengine.ext import ndb

class User(ndb.Model):
    user_name =  ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    user_nickname =  ndb.StringProperty(required=True)
    highscore =  ndb.IntegerProperty(default = 0)
    QCoins = ndb.IntegerProperty(default = 50)
    friends = ndb.KeyProperty(kind='User', repeated=True, required=False)
