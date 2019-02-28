"""
This module implements webapp commands.

@author: {{ cookiecutter.author }}
"""


import click
from flask.cli import AppGroup

{{ cookiecutter.package_slug }}_cli =  AppGroup({{ cookiecutter.package_slug }})


