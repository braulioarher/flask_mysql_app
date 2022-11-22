from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from roomapp.forms import UserForm
from roomapp.models import Users

from . import auth
from roomapp.models import db

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = UserForm()
    if signup_form.validate_on_submit():
        email = Users.query.filter_by(email=signup_form.email.data).first()
        username = Users.query.filter_by(username=signup_form.username.data).first()
        if email is None and username is None:
            hashed_pw = generate_password_hash(signup_form.password_hash.data, 'sha256')
            user = Users(username=signup_form.username.data, email=signup_form.email.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
            #login_user(user)
            flash('Bienvenido')
            return redirect(url_for('main.index'))
        else:
            if email is not None and username is not None:
                flash(f'Username: {signup_form.username.data} and Email: {signup_form.email.data} already exist in the data base')
                flash(email)
            elif username is not None:
                flash(f'Username: {signup_form.username.data} already exists in the database')
            elif email is not None:
                flash(f'Email: {signup_form.email.data} already exists in the database')
    contex = {
        'signup_form' : signup_form
    }
    return render_template('signup.html', **contex)


