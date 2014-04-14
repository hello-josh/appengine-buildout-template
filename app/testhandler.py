# demo handlers file
import webapp2
from webapp2_extras import jinja2


def jinja2_factory(app):
    """Creates the jinja2 instance and sets up any tests, filters, and global functions

    :param app: The WSGI app
    :type app: webapp2.WSGIApplication
    :return: configured Jinja2 instance
    :rtype: jinja2.Jinja2
    """
    j = jinja2.Jinja2(app)
    j.environment.filters.update({
    })
    j.environment.globals.update({
        'uri_for': webapp2.uri_for,
    })
    j.environment.tests.update({
    })
    return j


class MyTestHandler(webapp2.RequestHandler):
    def get(self):
        renderer = jinja2.get_jinja2(
            factory=jinja2_factory,
            app=self.app
        )
        self.response.write(renderer.render_template('index.html'))