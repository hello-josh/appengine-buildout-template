# demo handlers file
import webapp2
from webapp2_extras import jinja2
import os


def jinja2_factory(app):
    """Creates the jinja2 instance and sets up any tests, filters, and global functions

    :param app: The WSGI app
    :type app: webapp2.WSGIApplication
    :return: configured Jinja2 instance
    :rtype: jinja2.Jinja2
    """
    j = jinja2.Jinja2(app)
    (version, ts) = os.environ.get('CURRENT_VERSION_ID').split('.')
    # local dev ends up being None.\d\d\d\d\d\d\d\d\d\d\d so convert str(None) to None
    if version == 'None':
        version = None
    j.environment.filters.update({
    })
    j.environment.globals.update({
        'uri_for': webapp2.uri_for,
        'CURRENT_VERSION_LABEL': version
    })
    j.environment.tests.update({
    })
    return j


class MyHandler(webapp2.RequestHandler):
    def get(self):
        renderer = jinja2.get_jinja2(
            factory=jinja2_factory,
            app=self.app
        )
        self.response.write(renderer.render_template('index.html'))