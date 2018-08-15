from google.appengine.api import users
from google.appengine.ext import ndb
from musiq_models import User

logout_url = users.create_logout_url('/')
login_url = users.create_login_url('/')

class high_score_holder():
    def __init__(self, user, score, time):
        self.user = user
        self.score = score
        self.time = time

def ordered_highscores():
    highscore_users = User.query().order(-User.highscore).fetch(limit=10)
    return [(user.user_nickname, user.highscore) for user in highscore_users]

def create_profile(current_user):
    profile_fields = {
        "sign_out": logout_url,
        "username": current_user.user_nickname,
        "user_name": current_user.user_name,
        "QCoins": current_user.QCoins,
        "email": current_user.email,
        "highscores": ordered_highscores()
    }
    return profile_fields
