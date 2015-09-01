#!/usr/bin/env python
#


import webapp2
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
																autoescape=True)




class Handler(webapp2.RequestHandler):
	def write(self, *a, **kwArgs):
		self.response.write(*a, **kwArgs)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def renderIt(self, template, **kwArgs):
		self.write(self.render_str(template, **kwArgs))

class MainPage(Handler):
	def get(self):
		items = self.request.get_all("food")
		self.renderIt("shopping_list.html", items=items)

class FizzBuzzHandler(Handler):
	def get(self):
		n = self.request.get('n',0)
		n = n and int(n)
		self.renderIt("fizzbuzz.html", n=n)


		

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/fizzbuzz', FizzBuzzHandler)
], debug=True)
