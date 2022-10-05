from roomapp import db

class Temperature(db.Model):
    Date = db.Column(db.Date, primary_key=True)
    DeviceID = db.Column(db.Integer)
    Temperature = db.Column(db.Float(10,2))

    def __repr__(self):

        return (f"<Date: {self.Date}, Temperature: {self.Temperature}>")