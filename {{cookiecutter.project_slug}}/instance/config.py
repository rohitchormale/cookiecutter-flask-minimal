"""
This config should not go under version control
"""

import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
Testing = True

# database
SQLALCHEMY_DATABASE_URI = "sqlite:///%s/instance/{{ cookiecutter.project_slug }}.sqlite3" % BASE_DIR
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Logging
import logging
LOG_FILE = "/tmp/{{ cookiecutter.project_slug }}.log"
LOG_SIZE= 1024*1024
LOG_LEVEL = logging.DEBUG