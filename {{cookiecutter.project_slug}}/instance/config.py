"""
Add dynamic config here. Do NOT commit this file in vcs.

@author: {{cookiecutter.author}}
"""

import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
Testing = True
SECRET_KEY = os.urandom(32) # same key will be used for csrf protection


# database
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "sqlite:///%s/instance/{{ cookiecutter.project_slug }}.sqlite3" % BASE_DIR # sqlite
# SQLALCHEMY_DATABASE_URI = "mysql://<username>:<password>@<host>/<database>" # mysql/mariadb


# Logging
import logging
LOG_FILE = "/tmp/{{ cookiecutter.project_slug }}.log"
LOG_SIZE= 1024*1024
LOG_LEVEL = logging.DEBUG