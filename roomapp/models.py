from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Temperature(db.Model):
    Date = db.Column(db.Date, primary_key=True)
    DeviceID = db.Column(db.Integer)
    Temperature = db.Column(db.Float(10,2))

    def __repr__(self):

        return (f"<Date: {self.Date}, Temperature: {self.Temperature}>")

class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.usename
        self.password = user_data.password

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash =  generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return(f"Username: {self.Username}, Email: {self.Email}")