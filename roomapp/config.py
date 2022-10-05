import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wsl_root:19983006aB@172.21.128.1/smartroom'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'


