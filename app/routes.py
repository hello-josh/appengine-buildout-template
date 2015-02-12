from webapp2 import Route
import handlers

_routes = [
    # add `Route` or `RedirectRoute` classes here
    Route('/', handlers.MyHandler, 'index')
]


def get_routes():
    """Gets the app's routes
    Returns
        :return: List of Route
        :rtype: list of webapp2.Route
    """
    return _routes


def add_routes(app):
    """Adds routes to the `webapp2.WSGIApplication`

    :param app: The WSGI app
    :type app: webapp2.WSGIApplication
    """
    for r in _routes:
        app.router.add(r)
