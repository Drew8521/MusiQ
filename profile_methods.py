from google.appengine.api import users
from google.appengine.ext import ndb
from LionHouse_models import User

logout_url = users.create_logout_url('/')
login_url = users.create_login_url('/')

class high_score_holder():
    def __init__(self, user, time):
        self.user = user
        self.time = time

def ordered_highscores(posts):
    ordered_scores = []
    for highscore in highscores:
        score_holder = User.query().filter(User.key == highscore.user).get().username
        formatted_posts.append(PPost(score_holder, post.time))
    return ordered_scores

def create_profile(current_user):
    profile_fields = {
        "sign_out": logout_url,
        "username": current_user.user_nickname,
        "user_name": current_user.user_name,
        "posts": ordered_highscores(User.query().order(User.highscore).fetch(limit=15))
    }
    return profile_fields
