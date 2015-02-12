import webapp2
import unittest2
import webtest
from main import app


class MyTest(unittest2.TestCase):

    def uri_for(self, *args, **kwargs):
        req = webapp2.Request.blank('/')
        req.app = app
        app.set_globals(app=app, request=req)
        return webapp2.uri_for(*args, **kwargs)

    def test_something(self):
        self.app = webtest.TestApp(app)
        response = self.app.get(self.uri_for('index'))
        self.assertEqual(response.status_int, 200)