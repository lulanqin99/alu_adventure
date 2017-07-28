import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb

class Cheep(ndb.Model):
    email = ndb.StringProperty()
    message = ndb.StringProperty()
    post_time = ndb.DateTimeProperty(auto_now_add=True)

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        cheep_query = Cheep.query().order(Cheep.post_time)  #can change order/filter
        cheep = cheep_query.fetch()
        #filer: cheep_query = Cheep.query().filter( Cheep email = "").order(Cheep.post_time)

        template = jinja_environment.get_template("templates/cheep.html")

        current_user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')

        template_vars = { #dictionary
            'current_user':current_user,
            'logout_url': logout_url,
            'login_url': login_url
}
        self.response.write(template.render(template_vars))
        #if current_user: # exist, then log out link  # %s is a string

    def post(self):
        message = self.request.get('message')

        # get info from api and save into the db
        current_user = str(users.get_current_user())
        email = str(current_user)
        #email = current_user.email()

        #create a new cheep
        cheep = Cheep(message=message,email=email)

        cheep.put()

        #create response
        self.redirect('/')

        #get post from the form and make it appear on homepage
        # retrieve from the db #do it in a forloop in the html

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
