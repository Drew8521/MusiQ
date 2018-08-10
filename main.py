#main.py
#the import section
import webapp2
import jinja2
import os

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

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/profile', Profile)#this maps the root url to the MainPage Handler
], debug=True)
