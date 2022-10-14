from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class TempForm(FlaskForm):
    DeviceID = StringField("Device ID", [validators.DataRequired(message="Te felicito")])
    Temperature = StringField("Temperature", [validators.DataRequired()])
    submit = SubmitField("Submit")

