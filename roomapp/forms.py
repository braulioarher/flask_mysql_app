from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TempForm(FlaskForm):
    DeviceID = StringField("Device ID")
    Temperature = StringField("Temperature")
    submit = SubmitField("Submit")
    
