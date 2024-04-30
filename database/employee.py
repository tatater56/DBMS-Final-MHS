import database.db as db

from util import validate_date, validate_int

def get_all():
    return db.select_all('employee')

def get_all_doctors():
    return db.select_all('doctor')

def get_all_admins():
    return db.select_all('admin')

def get_all_nurses():
    return db.select_all('nurse')

def get_all_hcps():
    return db.select_all('otherhcp')



def get(EmpID):
    return db.select('employee', 'EmpID', EmpID)

def get_doctor(EmpID):
    return db.select('doctor', 'EmpID', EmpID)

def get_admin(EmpID):
    return db.select('admin', 'EmpID', EmpID)

def get_nurse(EmpID):
    return db.select('nurse', 'EmpID', EmpID)

def get_hcp(EmpID):
    return db.select('otherhcp', 'EmpID', EmpID)



def create(employee):
    print(f"employee.create({employee}) called!")

    if(not employee or not isinstance(employee, dict)):
        return False
    
    job_class = employee.get('JobClass', '')
    job_class_params = {}
    job_class_table = ''

    # Need to set empty dates to None to satisfy DataError mysql exception (will insert NULL into database)
    # mysql.connector.errors.DataError: 1292 (22007): Incorrect date value: '' for column `mhs`.`employee`.`HireDate` at row 1
    employee['HireDate'] = validate_date(employee.get('HireDate', None))

    # Need to set numbers to None too
    # mysql.connector.errors.DataError: 1366 (22007): Incorrect integer value: '' for column `mhs`.`employee`.`SSN` at row 1
    employee['SSN'] = validate_int(employee.get('SSN', None))

    match job_class:
        case 'Doctor':
            job_class_params['Specialty'] = employee.pop('Specialty', None)
            job_class_params['BC_Date'] = validate_date(employee.pop('BC_Date', None))
            job_class_table = 'doctor'

        case 'Nurse':
            job_class_params['Certification'] = employee.pop('Certification', None)
            job_class_table = 'nurse'

        case 'Other HCP':
            job_class_params['JobTitle'] = employee.pop('JobTitle', None)
            job_class_table = 'otherhcp'

        case 'Admin':
            job_class_params['JobTitle'] = employee.pop('JobTitle', None)
            job_class_table = 'admin'

        case _:
            print("Invalid JobClass! (" + job_class + ")")
            return False
    


    cnx = db.get_connection()

    if(cnx and cnx.is_connected()):
        with cnx.cursor(dictionary = True) as cursor:
            # https://blog.finxter.com/5-best-ways-to-insert-python-dictionaries-into-mysql/

            # Insert values in employee table
            placeholders = ', '.join(['%s'] * len(employee))
            columns = ', '.join(employee.keys())
            sql = "INSERT INTO employee (%s) VALUES (%s)" % (columns, placeholders)

            print("sql:")
            print(sql)
            print("employee.values():")
            print(employee.values())

            cursor.execute(sql, list(employee.values()))

            # Insert values in job class table
            EmpID = cursor.lastrowid
            job_class_params['EmpID'] = EmpID

            placeholders = ', '.join(['%s'] * len(job_class_params))
            columns = ', '.join(job_class_params.keys())
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (job_class_table, columns, placeholders)

            cursor.execute(sql, list(job_class_params.values()))
        cnx.commit()
        cnx.close()
    
    return job_class_params['EmpID']


def update(employee):
    print("employee.update() called!")

def delete(id):
    print("employee.delete() called!")
