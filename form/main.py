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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/form+results.html")
        self.response.write(template.render())

    def post(self):
        results_vars = {
            "noun1": self.request.get('noun1'),
            "noun2": self.request.get('noun2'),
            "adjective": self.request.get('adjective'),
            "noun3": self.request.get('noun3'),
            "box": self.request.get('box')
        }
        template = jinja_environment.get_template("templates/results.html")
        self.response.write(template.render(results_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
