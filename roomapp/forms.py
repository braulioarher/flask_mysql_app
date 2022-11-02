from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class TempForm(FlaskForm):
    DeviceID = StringField("Device ID", [validators.DataRequired(message="Te felicito")])
    Temperature = StringField("Temperature", [validators.DataRequired()])
    submit = SubmitField("Submit")

class UserForm(FlaskForm):
    Username = StringField('Username', [validators.DataRequired()])
    Email = StringField('Email', [validators.DataRequired()])
    submit = SubmitField('Submit')

