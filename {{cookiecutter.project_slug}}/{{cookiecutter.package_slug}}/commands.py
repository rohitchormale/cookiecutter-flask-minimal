"""
This module implements flask-cli commands.

@author: {{ cookiecutter.author }}
"""


import click
from flask.cli import AppGroup

{{ cookiecutter.package_slug }}_cli = AppGroup("{{ cookiecutter.package_slug }}")


"""
Example command

@{{ cookiecutter.package_slug }}_cli.command("add-user")
@click.option("--arg1")
@click.option("--arg2")
@click.option("--arg3")
def add_user(arg1, arg2, arg3):
    print("Command executed successfully")
"""
