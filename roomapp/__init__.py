from flask import Flask
from .config import BaseConfig
from flask_bootstrap import Bootstrap
from ensurepip import bootstrap
from flask_migrate import Migrate
from .models import db
import pymysql
from flask_apscheduler import APScheduler

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    #migrate = Migrate(app, db)
    bootstrap = Bootstrap(app)

    db.app = app
    db.init_app(app)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import routes

    app.register_blueprint(routes.mainBP, url_prefix='/')

    return app




from roomapp import routes

