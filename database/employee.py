import database.db as db

def get_all():
    print("employee.get_all() called!")
    
    results = []
    cnx = db.get_connection()

    if(cnx and cnx.is_connected()):
        with cnx.cursor() as cursor:
            cursor.execute("select * from employee;")
            results = cursor.fetchall()
        cnx.close()
    
    return results

def create(employee):
    print("employee.create() called!")

def update(employee):
    print("employee.update() called!")

def delete(id):
    print("employee.delete() called!")
