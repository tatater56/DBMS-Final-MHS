import database.db as db

from util import validate_form_input

def get_all():
    print("insurance.get_all() called!")
    return db.select_all('insurancecompany')

def get(Ins_id):
    print(f"insurance.get({Ins_id} called!)")
    return db.select('insurancecompany', 'Ins_id', Ins_id)

def create(insurance):
    print(f"insurance.create({insurance}) called!")

    if(not insurance or not isinstance(insurance, dict)):
        return False
    
    validate_form_input(insurance)
    return db.insert('insurancecompany', insurance)

def update(insurance):
    pass

def delete(id):
   return db.delete('insurancecompany', 'Ins_id', id)
    