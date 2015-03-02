import cherrypy

import random
import string


class StringGenerator(object):
  @cherrypy.expose()
  def index(self):
      return """
      <html>
        <head>
          <link href="static/css/style.css" rel="stylesheet">
        </head>
        <body>
          <h1>Random String Generator</h1>
          <form method="get" action="generate">
            String Length <input type="text" value="8" name="length" />
            <button type="submit">Give it now!</button>
          </form>
        </body>
      </html>
      """

  @cherrypy.expose()
  def generate(self, length=8):
      some_string = ''.join(random.sample(string.hexdigits, int(length)))
      cherrypy.session['mystring'] = some_string
      return some_string

  @cherrypy.expose()
  def display(self):
      return cherrypy.session['mystring']

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator(), '/', "app.conf")