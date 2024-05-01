import database.db as db

from util import validate_int, validate_form_input

def get_all():
    print("patient.get_all() called!")
    return db.select_all('patient')

def get(P_id):
    print(f"patient.get({P_id} called!)")
    return db.select('patient', 'P_id', P_id)

def create(patient):
    print(f"patient.create({patient}) called!")

    if(not patient or not isinstance(patient, dict)):
        return False
    
    patient['Ins_id'] = validate_int(patient.get('Ins_id', None))
    patient['PrimaryDoctorID'] = validate_int(patient.get('PrimaryDoctorID', None))

    validate_form_input(patient)
    return db.insert('patient', patient)

def update(patient):
    pass

def delete(id):
   return db.delete('patient', 'P_id', id)
    