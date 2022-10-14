from ensurepip import bootstrap
from sched import scheduler
from flask import Flask
from flask import render_template, request
from .config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import pymysql

from .models import db

from flask_apscheduler import APScheduler

app = Flask(__name__)
app.config.from_object(BaseConfig)
# db = SQLAlchemy()
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

db.app = app
db.init_app(app)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

app.run

from roomapp import routes

