import os
from roomapp.jobs import log_temp
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wsl_root:19983006aB@192.168.32.1/smartroom'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'


    JOBS = [{"id":"job100", "func": log_temp, "replace_existing":True, "trigger": "cron", "minute": "0,5,10,15,20,25,30,35,40,45,50,55"}]
    SCHEDULER_JOBSTORES = {
        "default": SQLAlchemyJobStore(url='mysql+pymysql://wsl_root:19983006aB@192.168.32.1/smartroom')
    }
    SCHEDULER_API_ENABLED = True

