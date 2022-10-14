import os
from .jobs import log_temp
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wsl_root:19983006aB@172.22.64.1/smartroom'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'


    JOBS = [{"id":"job100", "func": log_temp, "replace_existing":True, "trigger": "interval", "minutes": 5}]
    SCHEDULER_JOBSTORES = {
        "default": SQLAlchemyJobStore(url='mysql+pymysql://wsl_root:19983006aB@172.22.64.1/smartroom')
    }
    SCHEDULER_API_ENABLED = True

