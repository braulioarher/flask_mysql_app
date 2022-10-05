from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TempForm(FlaskForm):
    Date = StringField("Date")
    DeviceID = StringField("Device ID")
    Temperature = StringField("Temperature")
    submit = SubmitField("Submit")
    
