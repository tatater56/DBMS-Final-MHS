import database.db as db

from util import validate_int, is_empty_string

def get_all():
    print("facility.get_all() called!")
    return db.select_all('facility')

def get_all_opses():
    return db.select_all('ops')

def get_all_offices():
    return db.select_all('office')

def get(FacID):
    print(f"facility.get({FacID} called!)")
    return db.select('facility', 'FacID', FacID)

def get_ops(FacID):
    return db.select('ops', 'FacID', FacID)

def get_office(FacID):
    return db.select('office', 'FacID', FacID)

def create(facility):
    print(f"facility.create({facility}) called!")

    if(not facility or not isinstance(facility, dict)):
        return False
    
    ftype = facility.get('FType', '')
    ftype_data = {}

    facility['Size'] = validate_int(facility.get('Size', None))

    match ftype:
        case 'OPS':
            ftype_data['Room_Count'] = validate_int(facility.pop('Room_Count', None))
            ftype_data['P_code'] = facility.pop('P_code', None)
            ftype_data['Description'] = facility.pop('Description', None)

        case 'Office':
            ftype_data['Office_Count'] = validate_int(facility.pop('Office_Count', None))

        case _:
            print("Invalid JobClass! (" + jobclass + ")")
            return False
    
    FacID = db.insert('facility', facility)

    if(FacID == -1):
        print("Error! Could not create facility.")
        return False
    
    ftype_data['FacID'] = FacID
    db.insert(ftype, ftype_data)

    return FacID

def update(facility):
    pass

def delete(id):
    facility = db.select('facility', 'FacID', id)
    ftype = str(facility.get('FType', '')).lower()
    
    if(not is_empty_string(ftype)):
        db.delete(ftype, 'FType', id)

    return db.delete('facility', 'FacID', id)
    