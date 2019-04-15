"""
App init module

@author: {{ cookiecutter.author }}
"""

from flask import Flask, redirect, url_for
import logging
import logging.handlers
from .extensions import *

from .routes import *


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")

    # logging
    handler = logging.handlers.RotatingFileHandler(app.config["LOG_FILE"], maxBytes=app.config["LOG_SIZE"])
    handler.setLevel(app.config["LOG_LEVEL"])
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s [%(pathname)s at %(lineno)s]: %(message)s", "%Y-%m-%d %H:%M:%S"))
    app.logger.addHandler(handler)

    # init
    db.init_app(app)

    with app.app_context():
        # TODO - register blueprints here. e.g.
        # from .routes import auth_blueprint
        # app.register_blueprint(auth_blueprint)



        # finally create tables as per models
        db.create_all()

        @app.route("/")
        def home():
            # TODO - add here endpoint of resource where you want to land on page load. e.g.
            # return redirect(url_for("auth_blueprint.home"))
            return redirect(url_for("index"))

    return app
