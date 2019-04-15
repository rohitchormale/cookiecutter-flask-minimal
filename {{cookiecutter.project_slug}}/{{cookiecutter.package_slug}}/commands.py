"""
This module implements webapp commands.

@author: {{ cookiecutter.author }}
"""


import click
from flask.cli import AppGroup

{{ cookiecutter.package_slug }}_cli = AppGroup("{{ cookiecutter.package_slug }}")


@{{ cookiecutter.package_slug }}_cli.command("test-command")
@click.option("--arg1")
@click.option("--arg2")
@click.option("--arg3")
def test_command(arg1, arg2, arg3):
    print("Command executed successfully")
