import database.db as db

from util import validate_datetime, validate_form_input

def get_all():
    print("appointment.get_all() called!")
    return db.select_all('makesappointment')

def get(AppID):
    print(f"appointment.get({AppID} called!)")
    return db.select('makesappointment', 'AppID', AppID)

def create(appointment):
    print(f"appointment.create({appointment}) called!")

    if(not appointment or not isinstance(appointment, dict)):
        return False
    
    appointment['Date_Time'] = validate_datetime(appointment.get('Date_Time', None))
    return db.insert('makesappointment', appointment)

def update(appointment):
    print(f"appointment.update({appointment}) called!")

    if(not appointment or not isinstance(appointment, dict)):
        return False
    
    appointment['Date_Time'] = validate_datetime(appointment.get('Date_Time', None))
    return db.update('makesappointment', 'AppID', appointment)

def delete(id):
   return db.delete('makesappointment', 'AppID', id)
    