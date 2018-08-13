#main.py
#the import section
import webapp2
import jinja2
import os
import time
from google.appengine.api import users
from google.appengine.ext import ndb
from musiq_models import User

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#the handler section
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')
        new_user_template = jinja_env.get_template("templates/new_user.html")
        prev_user_template = jinja_env.get_template("templates/prev_user.html")
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
        else:
            # Ask user to sign in to Google
            self.response.write(google_login_template.render({ "login_url": login_url }))


class Profile(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/profile.html')
        self.response.write(template.render({"sign_out": users.create_logout_url('/')}))

    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect('/')
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

class GenreChooser(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/genre_chooser.html')
        self.response.write(template.render())

class DifficultyChooser(webapp2.RequestHandler):
    def get(self):
        template=jinja_env.get_template('/templates/difficulty_chooser.html')
        self.response.write(template.render())

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/profile', Profile),
    ('/genre-chooser', GenreChooser),
    ('/difficulty-chooser', DifficultyChooser)#this maps the root url to the MainPage Handler
], debug=True)
