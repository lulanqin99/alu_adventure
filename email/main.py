#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Email:
    def __init__(self, subject, mailfrom ):
        self.subject = subject
        self.mailfrom = mailfrom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        mail: [
            Email("")
        ]


        template = jinja_environment.get_template("templates/cssi.html")
        self.response.write(template.render(cssi_vars))

class InboxHandler(webapp2.RequestHandler):
    def get(self):
        subject = self.request.get('subject')
        mailfrom = self.request.get('mailfrom')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/inbox', InboxHandler),
], debug=True)
