from crypt import methods
from datetime import datetime
from multiprocessing import context
from flask import Blueprint, Flask, render_template, request, flash, make_response
from roomapp import db
from roomapp.models import Temperature, Users
from .forms import TempForm, UserForm, PasswordForm
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
    if user_form.validate_on_submit():
        user = Users.query.filter_by(email=user_form.email.data).first()
        flash("Form submitted")
        if user is None:
            hashed_pw = generate_password_hash(user_form.password_hash.data, "sha256")
            user = Users(name=user_form.Username.data, email=user_form.email.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        username = user_form.Username.data
        user_form.username.data = ''
        user_form.email.data = ''
        user_form.password_hash.data = ''
    our_users = Users.query.order_by(Users.id)
    context = {
        'title' : 'User List',
        'user_form' : user_form,
        'our_users' : our_users
    }
    return render_template('adduser.html', **context)

@mainBP.route('/test_pw/', methods=['GET', 'POST'])
def test_pw():
    email = None
    password = None
    pw_to_check = None
    passed = None
    form  = PasswordForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password_hash.data
        #Limpia el formulario
        form.email.data = ''
        form.password_hash.data = ''

        pw_to_check = Users.query.filter_by(email=email).first()

        # Verificar password
        passed = check_password_hash(pw_to_check.password_hash, password)
    context = {
        'title' : 'Check Password',
        'form' : form,
        'email' : email,
        'password' : password ,
        'pw_to_check' : pw_to_check,
        'passed' : passed
    }
    return render_template("test_pw.html", **context)

# Seccion de documentos de flask

@mainBP.route('/createapp')
def crearapp():
    return render_template('crearapp.html')

@mainBP.route('/configfile')
def configfile():
    return render_template('configfile.html')

@mainBP.route('/modelsfile')
def modelsfile():
    return render_template('modelsfile.html')

@mainBP.route('/formsfile')
def formsfile():
    return render_template('formsfile.html')

@mainBP.route('/routesfile')
def routesfile():
    return render_template('routesfile.html')

#Seccion de modulos de flask

@mainBP.route('/notas/')
def notas():
    return render_template('notas.html')

@mainBP.route('/flaskcli')
def flaskcli():
    return render_template('flaskcli.html')

@mainBP.route('/filtros')
def filtros():
    return render_template('filtros.html')

@mainBP.route('/cookies')
def cookies():
    return render_template('cookies.html')

@mainBP.route('/session')
def session():
    return render_template('session.html')

# Seccion de ejercios de Flask

@mainBP.route('/restapi')
def restapi():
    return render_template('restapi.html')


# Seccion notas 

@mainBP.route('/request')
def request():
    return render_template('request.html')

@mainBP.route('/jsonify')
def jsonify():
    return render_template('jsonify.html')

@mainBP.route('/httprequest')
def httprequest():
    return render_template('httprequest.html')

@mainBP.route('/httpcodes')
def httpcodes():
    return render_template('httpcodes.html')


@mainBP.route('/consultadb')
def consultadb():
    return render_template('consultadb.html')

@mainBP.route('/sessionmaker')
def sessionmaker():
    return render_template('sessionmaker.html')

@mainBP.route('/jwt')
def jwt():
    return render_template('jwt.html')



@mainBP.route('/setcookie/')
def setcookie():
    resp = make_response("<h2>La cookie 'holacookie' se configuro")
    resp.set_cookie('holacookie', 'hola')
    return resp

@mainBP.route('/getcookie/')
def getcookie():
    cookie1 = request.cookies.get('holacookie')
    return(f"'holacookie' dice: {cookie1}")


app.register_blueprint(mainBP)