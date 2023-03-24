from flask import Flask
from flask_bootstrap import Bootstrap
from flask_apscheduler import APScheduler
from flask_login import LoginManager
from flask_migrate import Migrate

from db import db
from .auth import auth
from .config import BaseConfig
from .models import db, UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth_login'

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    bootstrap = Bootstrap(app)

    db.init_app(app)

    migrate = Migrate(app, db)


    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import routes

    app.register_blueprint(routes.mainBP, url_prefix='/')
    app.register_blueprint(auth)

    return app




from roomapp import routes

