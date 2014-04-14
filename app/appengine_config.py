"""`appengine_config` gets loaded when starting a new application instance."""
import sys
import os.path
# add `dist` subdirectory to `sys.path`, so our `main` module can load
# `zc.buildout` installed libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'dist'))
