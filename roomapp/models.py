from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Temperature(db.Model):
    Date = db.Column(db.Date, primary_key=True)
    DeviceID = db.Column(db.Integer)
    Temperature = db.Column(db.Float(10,2))

    def __repr__(self):

        return (f"<Date: {self.Date}, Temperature: {self.Temperature}>")

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __repr__(self):
        return(f"Username: {self.Username}, Email: {self.Email}")