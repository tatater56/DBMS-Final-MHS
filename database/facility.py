import database.db as db

def get_all():
    print("facility.get_all() called!")
    return db.select_all('facility')

def get(FacID):
    print(f"facility.get({FacID} called!)")
    return db.select('facility', 'FacID', FacID)
    