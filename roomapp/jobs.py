from datetime import datetime
import random
from roomapp.models import Temperature, db

def log_temp():
    with db.app.app_context():
        try:
            entero = random.randrange(20, 25)
            deci = random.random()
            temperature = round(entero + deci, 2)
            record = Temperature(Date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), DeviceID=2, Temperature=temperature)
            db.session.add(record)
            db.session.commit()
            print("Temperatura registrada")
        except Exception:
            db.session.rollback()
