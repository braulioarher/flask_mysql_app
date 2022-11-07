from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length

class TempForm(FlaskForm):
    DeviceID = StringField("Device ID", [DataRequired(message="Te felicito")])
    Temperature = StringField("Temperature", [DataRequired()])
    submit = SubmitField("Submit")

class UserForm(FlaskForm):
    Username = StringField('Username', [DataRequired()])
    Email = StringField('Email', [DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PasswordForm(FlaskForm):
    email = StringField("What is your Email", validators=[DataRequired()])
    password_hash = PasswordField("What's your Password", validators=[DataRequired()])
    submit = SubmitField('Sign in')