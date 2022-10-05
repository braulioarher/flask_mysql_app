from crypt import methods
from datetime import datetime
from roomapp import app, db
from roomapp import render_template, request
from roomapp.models import Temperature
from .forms import TempForm
from datetime import datetime

@app.route('/')
def index():
    return("<h1>Bienvenido</h1>")

@app.route('/showtemperatures/')
def showtemp():
    temps = Temperature.query.all()
    temps = [round(tempe.Temperature, 2) for tempe in temps]
    return render_template('showtemp.html', temps=temps)

@app.route("/addtemp/", methods=['GET', 'POST'])
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
