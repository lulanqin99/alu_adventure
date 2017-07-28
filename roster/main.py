import webapp2
import jinja2
import os

from google.appengine.ext import ndb #newdatabasea

class Person(ndb.Model):
    color = ndb.StringProperty()
    name = ndb.StringProperty()
    university = ndb.StringProperty()


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # 1. query and fetch the values from the database
        person_query = Person.query()
        person = person_query()
        # 2. store values in a dictionary
        person_vars = {
            "person:" person
        }

        # 3. pass it into template.render [loop each student and print their properties]




        template = jinja_environment.get_template("templates/form.html")
        self.response.write(template.render(person_vars))

    def post(self):
        # 1. get info and submit into form
        name = self.request.get('name')
        university = self.request.get ('university')
        color = self.request.get('color')

        # 2. put into a new person Model
        person = Person(name=name,university=university,color=color)

        # 3. save that person into database
        person.put()

        # 4. redirect to home
        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
