from crypt import methods
from datetime import datetime
from multiprocessing import context
from flask import Blueprint, Flask, render_template, request, flash
from roomapp import db
from roomapp.models import Temperature, Users
from .forms import TempForm, UserForm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

mainBP = Blueprint(
    'main',
    __name__,
    template_folder='templates'
)

@mainBP.app_errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)

@mainBP.app_errorhandler(500)
def server_error(error):
    return render_template('500.html', error = error)

@mainBP.route('/')
def index():
    context = {
        'title' : 'Home'
    }
    return render_template('index.html', **context)

@mainBP.route('/showtemperatures/')
def showtemp():
    data = Temperature.query.all()
    temps = [round(tempe.Temperature, 2) for tempe in data]
    labels = [str(item.Date) for item in data]
    values = [int(item) for item in temps]
    context = {
        'title' : 'Show Temperatures',
        'temps' : temps,
        'labels': labels,
        'values': values
    }
    return render_template('showtemp.html', **context)

@mainBP.route("/addtemp/", methods=['GET', 'POST'])
def addtemp():
    form = TempForm()
    if request.method == 'POST':
        datenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp =  Temperature(Date=datenow, DeviceID=int(form.DeviceID.data), Temperature=float(form.Temperature.data))
        try:
            db.session.add(temp)
            db.session.commit()
            return render_template('addtemp_confirmation.html')
        except Exception:
            db.session.rollback()
        
    return render_template('addtemp.html', form=form)

@mainBP.route("/addtempwtf/", methods=['GET', 'POST'])
def addtempwtf():
    temp_form = TempForm()
    if request.method == 'POST':
        datenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp =  Temperature(Date=datenow, DeviceID=int(temp_form.DeviceID.data), Temperature=float(temp_form.Temperature.data))
        try:
            db.session.add(temp)
            db.session.commit()
            return render_template('addtemp_confirmation.html')
        except Exception:
            db.session.rollback()
    context = {
        'title' : 'Add New Temperature',
        'temp_form' : temp_form
    }
        
    return render_template('addtempwtfquick.html', **context)

@mainBP.route('/adduser/', methods=['GET', 'POST'])
def adduser():
    user_form = UserForm()
    if request.method == 'POST':
        user = Users.query.filter_by(email=user_form.Email.data).first()
        flash("Form submitted")
        if user is None:
            hashed_pw = generate_password_hash(user_form.password_hash.data, "sha256")
            user = Users(name=user_form.Username.data, email=user_form.Email.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        username = user_form.Username.data
        user_form.Username.data = ''
        user_form.Email.data = ''
        user_form.password_hash.data = ''
    our_users = Users.query.order_by(Users.id)
    context = {
        'title' : 'User List',
        'user_form' : user_form,
        'our_users' : our_users
    }
    return render_template('adduser.html', **context)

app.register_blueprint(mainBP)