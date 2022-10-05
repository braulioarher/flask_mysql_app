from flask import Flask
from flask import render_template, request
from .config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql



app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from roomapp import routes