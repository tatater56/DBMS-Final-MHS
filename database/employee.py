import database.db as db

from util import validate_date, validate_int, is_empty_string

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


def get_employee_jobclass_data(EmpID, JobClass):
    if is_empty_string(EmpID) or is_empty_string(JobClass):
        return {}
    
    job_class_table = ''
    
    match JobClass:
        case 'Doctor':
            job_class_table = 'doctor'

        case 'Nurse':
            job_class_table = 'nurse'

        case 'Other HCP':
            job_class_table = 'otherhcp'

        case 'Admin':
            job_class_table = 'admin'

        case _:
            job_class_table = None
    
    if(job_class_table):
        return db.select(job_class_table, 'EmpID', EmpID)
    else:
        return {}


def create(employee):
    print(f"employee.create({employee}) called!")

    if(not employee or not isinstance(employee, dict)):
        return False
    
    jobclass = employee.get('JobClass', '')
    jobclass_data = {}

    # Need to set empty dates to None to satisfy DataError mysql exception (will insert NULL into database)
    # mysql.connector.errors.DataError: 1292 (22007): Incorrect date value: '' for column `mhs`.`employee`.`HireDate` at row 1
    employee['HireDate'] = validate_date(employee.get('HireDate', None))

    # Need to set numbers to None too
    # mysql.connector.errors.DataError: 1366 (22007): Incorrect integer value: '' for column `mhs`.`employee`.`SSN` at row 1
    employee['SSN'] = validate_int(employee.get('SSN', None))

    match jobclass:
        case 'Doctor':
            jobclass_data['Specialty'] = employee.pop('Specialty', None)
            jobclass_data['BC_Date'] = validate_date(employee.pop('BC_Date', None))
            jobclass = 'doctor'

        case 'Nurse':
            jobclass_data['Certification'] = employee.pop('Certification', None)
            jobclass = 'nurse'

        case 'Other HCP':
            jobclass_data['JobTitle'] = employee.pop('JobTitle', None)
            jobclass = 'otherhcp'

        case 'Admin':
            jobclass_data['JobTitle'] = employee.pop('JobTitle', None)
            jobclass = 'admin'

        case _:
            print("Invalid JobClass! (" + jobclass + ")")
            return False
    
    EmpID = db.insert('employee', employee)

    if(EmpID == -1):
        print("Error! Could not create employee.")
        return False
    
    jobclass_data['EmpID'] = EmpID
    db.insert(jobclass, jobclass_data)

    return EmpID


def update(employee):
    print(f"employee.update({employee}) called!")

    if(not employee or not isinstance(employee, dict)):
        return False

    # Validate date and int
    employee['HireDate'] = validate_date(employee.get('HireDate', None))
    employee['SSN'] = validate_int(employee.get('SSN', None))

    return db.update('employee', 'EmpID', employee)

def update_employee_jobclass(jobclass_data):
    print(f"employee.update_employee_jobclass({jobclass_data}) called!")

    if(not jobclass_data or not isinstance(jobclass_data, dict)):
        return False

    NewJobClassAttr = jobclass_data.get('NewJobClass', None)
    NewJobClass = _jobclass_to_table_name(jobclass_data.pop('NewJobClass', None))
    OldJobClass = _jobclass_to_table_name(jobclass_data.pop('OldJobClass', None))
    EmpID = jobclass_data.get('EmpID', None)

    if is_empty_string(NewJobClass) or is_empty_string(OldJobClass) or is_empty_string(EmpID):
        return False

    # Validate BC_Date for doctors
    BC_Date = jobclass_data.get('BC_Date', None)
    if(BC_Date):
        jobclass_data['BC_Date'] = validate_date(BC_Date)

    # If not changing jobclass, update
    if(NewJobClass == OldJobClass):
        print("Keeping same jobclass")
        db.update(NewJobClass, 'EmpID', jobclass_data)
    # Else, delete old jobclass and insert new
    else:
        print(f"Changing jobclass {OldJobClass} to {NewJobClass}")
        db.insert(NewJobClass, jobclass_data)
        db.delete(OldJobClass, 'EmpID', EmpID)
        db.update('employee', 'EmpID', {'EmpID': EmpID, 'JobClass':NewJobClassAttr})
    
    return True


def delete(id):
    employee = db.select('employee', 'EmpID', id)
    jobclass = _jobclass_to_table_name(employee.get('JobClass', None))
    
    if(jobclass):
        db.delete(jobclass, 'EmpID', id)

    return db.delete('employee', 'EmpID', id)


def _jobclass_to_table_name(jobclass):
    match jobclass:
        case 'Doctor':
            return 'doctor'

        case 'Nurse':
            return 'nurse'

        case 'Other HCP':
            return 'otherhcp'

        case 'Admin':
            return 'admin'

        case _:
            return None
