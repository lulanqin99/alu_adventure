import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Post(ndb.Model):
    author = ndb.StringProperty()
    post_time = ndb.DateTimeProperty(auto_now_add=True)
    content = ndb.StringProperty()
    title = ndb.StringProperty()

class Comment(ndb.Model):
    author = ndb.StringProperty()#from form
    post_time = ndb.DateTimeProperty(auto_now_add=True)#fromndb
    content = ndb.StringProperty()#from form
    post_key = ndb.KeyProperty(kind=Post)#from form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        post_query = Post.query().order(-Post.post_time)#reverseChron
        posts = post_query.fetch()

        template = jinja_environment.get_template("templates/home.html")

        template_vars = {
            'posts': posts
        }
        self.response.write(template.render(template_vars))

class PostHandler(webapp2.RequestHandler):
    def get(self):
        # 1. get info from the request
        urlsafe_key = self.request.get('key') #getkeyout of url
        # 2. pulling post from the database
        post_key = ndb.Key(urlsafe=urlsafe_key) #transfrom to post obj
        post = post_key.get() # then get it
        # 3. rendering the template to the response  #can go back and forth key to post and vice versa

#load comments and pass thru template vars

        comment_query = Comment.query()
        comment_query = comment_query.filter(Comment.post_key == post_key)
        comment_query = comment_query.order(-Comment.post_time)
        comments = comment_query.fetch()

        template_vars = {
            'post':post,
            'comments':comments,
        }
        template = jinja_environment.get_template("templates/post.html")
        self.response.write(template.render(template_vars))

class NewPostHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/new_post.html")
        self.response.write(template.render())

    def post(self):
        # 1. getting info from request(form)
        title = self.request.get('title')
        content = self.request.get('content')
        # 2. interacting with database and api
        current_user = users.get_current_user()
        author = current_user.email()

        # 3. set_up new post
        post = Post(title=title,content=content, author=author)
        # 4. put it back into the database
        post.put()
        #5
        #self.response.write('you made a new post')
        self.redirect('/')

class NewCommentHandler(webapp2.RequestHandler):
    def post(self):
        # 1. Get info from the request.
        author = self.request.get('author')
        content = self.request.get('content')
        urlsafe_key = self.request.get('post_key')

        # 2. Use the info and interact with the database
        post_key = ndb.Key(urlsafe=urlsafe_key)
        post = post_key.get()

        comment = Comment(post_key=post_key,content=content,author=author)
        comment.put()
        # 3. Send a response.
        url = '/post?key=' + post.key.urlsafe()
        self.redirect(url)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/post', PostHandler),
    ('/new_post', NewPostHandler),
    ('/new_comment', NewCommentHandler)
], debug=True)
