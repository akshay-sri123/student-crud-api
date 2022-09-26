from flask import Flask
import logging

from .models import db, migrate
from . import config

def create_app():
    flask_app = Flask(__name__)
    flask_app.logger.setLevel(logging.DEBUG)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    migrate.init_app(flask_app, db)
    return flask_app