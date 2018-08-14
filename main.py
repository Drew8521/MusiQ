#main.py
#the import section
import webapp2
import jinja2
import os
import time
from google.appengine.api import users
from google.appengine.ext import ndb
from musiq_models import User
from profile_methods import create_profile, logout_url, login_url

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#the handler section
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        new_user_template = jinja_env.get_template("templates/new_user.html")
        google_login_template = jinja_env.get_template("templates/google_login.html")
        # get Google user
        user = users.get_current_user()

        if user:
            # look for user in datastore
            existing_user = User.query().filter(User.email == user.email()).get()
            nickname = user.nickname()
            if not existing_user:
                fields = {
                  "nickname": nickname,
                  "logout_url": logout_url,
                }
                # prompt new users to sign up
                self.response.write(new_user_template.render(fields))
            else:
                # direct existing user to feed
                self.redirect('/profile')
                return
        else:
            # Ask user to sign in to Google
            self.response.write(google_login_template.render({ "login_url": login_url }))


class Profile(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/profile.html')
        user = users.get_current_user()
        current_user = User.query().filter(User.email == user.email()).get()
        profile_fields = create_profile(current_user)
        self.response.write(template.render(profile_fields))

    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect('/')
            return
        current_user = User.query().filter(User.email == user.email()).get()
        if not current_user:
            # upon new user form submission, create new user and store in datastore
            new_user_entry = User(
            user_name = self.request.get("name"),
            user_nickname = self.request.get("username"),
            email = user.email(),
            )
            new_user_entry.put()
            current_user = new_user_entry
        time.sleep(.2)
        self.redirect('/profile')
        return

class GenreChooser(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/genre_chooser.html')
        self.response.write(template.render())

class DifficultyChooser(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/difficulty_chooser.html')
        self.response.write(template.render())

class SeedHandler(webapp2.RequestHandler):
    def get(self):
        new_user_entry = User(
        user_name = "Arthur",
        user_nickname = "Giggle",
        email = "asdf@asdf.com",
        highscore = 12
        )
        new_user_entry.put()
        new_user_entry = User(
        user_name = "Dalman",
        user_nickname = "DaMan",
        email = "asd@asdf.com",
        highscore = 19
        )
        new_user_entry.put()
        new_user_entry = User(
        user_name = "Sal",
        user_nickname = "NotSal",
        email = "IActuallyAmSal@asdf.com",
        highscore = 42
        )
        new_user_entry.put()
        new_user_entry = User(
        user_name = "SerialKiller",
        user_nickname = "DefNotAKiller",
        email = "Puppies@asdf.com",
        highscore = 39
        )
        new_user_entry.put()
        new_user_entry = User(
        user_name = "JohnCena",
        user_nickname = "CenaYouCenaMe",
        email = "YouCantSeeMe@asdf.com",
        highscore = 104
        )
        new_user_entry.put()
#the app configuration section
app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/seed', SeedHandler),
    ('/profile', Profile),
    ('/genre-chooser', GenreChooser),
    ('/difficulty-chooser', DifficultyChooser)#this maps the root url to the MainPage Handler
], debug=True)
