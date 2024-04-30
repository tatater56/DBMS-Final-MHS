import database.db as db

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
    pass

def update(facility):
    pass

def delete(id):
    pass
    