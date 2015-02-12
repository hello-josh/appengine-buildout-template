# config options for your app
import os
webapp2_config = {
    'webapp2_extras.jinja2': {
        'template_path': os.path.join(os.path.dirname(__file__), 'templates')
    }
}