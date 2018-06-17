from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_bootstrap import Bootstrap

from .config import config_by_name
from .nav import nav

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
socketio = SocketIO()
bootstrap = Bootstrap()
cors = CORS()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    cors.init_app(app)
    bootstrap.init_app(app)
    socketio.init_app(app)
    nav.init_app(app)

    return app

