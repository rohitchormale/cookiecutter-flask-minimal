"""
wsgi application instance to deploy app behind apache/gunicorn/nginx

@author: {{ cookiecutter.author }}
"""

import os, sys
app_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_path)


from {{cookiecutter.package_slug}} import create_app
application = create_app()