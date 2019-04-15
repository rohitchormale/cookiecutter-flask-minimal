"""
This config should not go under version control
"""
DEBUG = True
Testing = True

# Logging
import logging
LOG_FILE = "/tmp/{{ cookiecutter.project_slug }}.log"
LOG_SIZE= 1024*1024
LOG_LEVEL = logging.DEBUG