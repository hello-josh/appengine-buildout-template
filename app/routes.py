from webapp2 import Route
import testhandler

_routes = [
    # add `Route` or `RedirectRoute` classes here
    Route('/', testhandler.MyTestHandler, 'index')
]


def get_routes():
    """Gets the app's routes

    :return: List of routes
    :rtype: list
    """
    return _routes


def add_routes(app):
    """Adds routes to the `webapp2.WSGIApplication`

    :param app: The WSGI app
    :type app: webapp2.WSGIApplication
    """
    for r in _routes:
        app.router.add(r)
