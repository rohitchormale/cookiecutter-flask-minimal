"""
To avoid cyclic imports, instantiate extensions here.
Use this module to access them elsewhere in project, instead using `__init__.py`
"""


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .models import *
