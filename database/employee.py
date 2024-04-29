import database.db as db

def get_all():
    print("employee.get_all() called!")
    
    results = []
    cnx = db.get_connection()

    if(cnx and cnx.is_connected()):
        with cnx.cursor(dictionary = True) as cursor:
            cursor.execute("select * from employee;")
            results = cursor.fetchall()
        cnx.close()
    
    return results

def get(EmpID):
    print(f"employee.get({EmpID} called!)")
    if(not EmpID or EmpID.isspace()):
        return {}

    result = {}
    cnx = db.get_connection()

    if(cnx and cnx.is_connected()):
        with cnx.cursor(dictionary = True) as cursor:
            cursor.execute(f"select * from employee where EmpID={EmpID};")
            result = cursor.fetchone()
        cnx.close()
    
    return result

def create(employee):
    print(f"employee.create({employee}) called!")
    if(not employee or not isinstance(employee, dict)):
        return False
    
    cnx = db.get_connection()

    if(cnx and cnx.is_connected()):
        with cnx.cursor(dictionary = True) as cursor:
            # https://blog.finxter.com/5-best-ways-to-insert-python-dictionaries-into-mysql/

            placeholders = ', '.join(['%s'] * len(employee))
            columns = ', '.join(employee.keys())
            sql = "INSERT INTO employee (%s) VALUES (%s)" % (columns, placeholders)

            cursor.execute(sql, list(employee.values()))
        cnx.close()


def update(employee):
    print("employee.update() called!")

def delete(id):
    print("employee.delete() called!")
