import webapp2
import config
import routes

app = webapp2.WSGIApplication(
    config=config.webapp2_config
)

routes.add_routes(app)
