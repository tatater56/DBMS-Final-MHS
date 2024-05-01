from flask import render_template, url_for, redirect, request
from __main__ import app

from database import db, employee, facility, insurance

import util

# Main page

@app.route('/EmployeeFacilityManagement')
def efm_page():
    return render_template('EmployeeFacilityManagement.html',
                            message = request.args.get("message", default = None),
                            employees = employee.get_all(),
                            doctors = employee.get_all_doctors(),
                            nurses = employee.get_all_nurses(),
                            admins = employee.get_all_admins(),
                            hcps = employee.get_all_hcps(),
                            facilities = facility.get_all(),
                            opses = facility.get_all_opses(),
                            offices = facility.get_all_offices(),
                            insurances = insurance.get_all())


# New employee

@app.route('/NewEmployee/<JobClass>')
def new_employee_page(JobClass):
    return render_template('employee/new.html',
                            JobClass=JobClass,
                            facilities=facility.get_all())

@app.route('/api/NewEmployee', methods=['POST'])
def api_new_employee():
    form_dict = {k: v for k, v in request.form.items()}
    result = employee.create(form_dict)
    if(result):
        message = f'New employee created (id:{result})'
    else:
        message = 'Error encountered while attempting to create employee!'

    return redirect(url_for('efm_page', 
                        message=message))

# Update employee

@app.route('/UpdateEmployee/<EmpID>')
def update_employee_page(EmpID):
    return render_template('employee/update.html',
                            employee = employee.get(EmpID),
                            facilities = facility.get_all())

@app.route('/api/UpdateEmployee', methods=['POST'])
def api_update_employee():
    form_dict = {k: v for k, v in request.form.items()}
    EmpID = employee.update(form_dict)

    if EmpID:
        result = f"Employee updated (id:{EmpID})"
    else:
        result = "Could not update employee"

    return redirect(url_for('efm_page',
                            message=result))

@app.route('/UpdateEmployeeJobClass/<EmpID>/<JobClass>')
def update_employee_jobclass_page(EmpID, JobClass):
    # Change 'HCP' to 'Other HCP'
    JobClass = 'Other HCP' if JobClass == 'HCP' else JobClass

    emp = employee.get(EmpID)
    OldJobClass = emp.get('JobClass', None)

    jobclass_data = {}
    if JobClass == OldJobClass:
        jobclass_data = employee.get_employee_jobclass_data(EmpID, JobClass)
    
    print("update_employee_jobclass_page called!\n"
            f"{EmpID=}, {JobClass=}, {OldJobClass=}, {jobclass_data=}")

    return render_template('employee/update_jobclass.html',
                            EmpID=EmpID,
                            OldJobClass=OldJobClass,
                            NewJobClass=JobClass,
                            jobclass_data=jobclass_data)

@app.route('/api/UpdateEmployeeJobClass', methods=['POST'])
def api_update_employee_jobclass():
    form_dict = {k: v for k, v in request.form.items()}

    result = employee.update_employee_jobclass(form_dict)

    message = ''
    if(result):
        message = 'Employee JobClass updated'
    else:
        message = 'Encountered an error while attempting Employee JobClass update'

    return redirect(url_for('efm_page',
                            message=message))


# Delete employee

@app.route('/DeleteEmployee/<EmpID>')
def delete_employee_page(EmpID):
    return render_template('employee/delete.html',
                            employee=employee.get(EmpID))

@app.route('/api/DeleteEmployee/<EmpID>')
def api_delete_employee(EmpID):
    if(util.is_empty_string(EmpID)):
        return redirect(url_for('efm_page',
                                message='Employee could not be deleted, no EmpID given'))
    else:
        result = ''
        if employee.delete(EmpID):
            result = f'Employee deleted (id:{EmpID})'
        else:
            result = f'Error encountered, could not delete employee (id:{EmpID})'
        
        return redirect(url_for('efm_page',
                                message=result))



# New facility

@app.route('/NewFacility/<FType>')
def new_facility_page(FType):
    return render_template('facility/new.html',
                            FType=FType)

@app.route('/api/NewFacility', methods=['POST'])
def api_new_facility():
    form_dict = {k: v for k, v in request.form.items()}

    result = facility.create(form_dict)
    if(result):
        message = f'New facility created (id:{result})'
    else:
        message = 'Error encountered while attempting to create facility!'

    return redirect(url_for('efm_page', 
                        message=message))

# Delete facility

@app.route('/DeleteFacility/<FacID>')
def delete_facility_page(FacID):
    return render_template('facility/delete.html',
                            facility=facility.get(FacID))

@app.route('/api/DeleteFacility/<FacID>')
def api_delete_facility(FacID):
    if(util.is_empty_string(FacID)):
        return redirect(url_for('efm_page',
                                message='Facility could not be deleted, no FacID given'))
    else:
        result = ''
        if facility.delete(FacID):
            result = f'Facility deleted (id:{FacID})'
        else:
            result = f'Error encountered, could not delete facility (id:{FacID})'
        
        return redirect(url_for('efm_page',
                                message=result))

# TODO: Update facility

# New insurance company

@app.route('/NewInsurance')
def new_insurance_page():
    return render_template('insurance/new.html')

@app.route('/api/NewInsurance', methods=['POST'])
def api_new_insurance():
    form_dict = {k: v for k, v in request.form.items()}

    result = insurance.create(form_dict)
    if(result):
        message = f'New insurance created (id:{result})'
    else:
        message = 'Error encountered while attempting to create insurance!'

    return redirect(url_for('efm_page', 
                        message=message))

# Delete insurance

@app.route('/api/DeleteInsurance/<Ins_id>')
def api_delete_insurance(Ins_id):
    if(util.is_empty_string(Ins_id)):
        return redirect(url_for('efm_page',
                                message='Insurance could not be deleted, no Ins_id given'))
    else:
        result = ''
        if insurance.delete(Ins_id):
            result = f'Insurance deleted (id:{Ins_id})'
        else:
            result = f'Error encountered, could not delete insurance (id:{Ins_id})'
        
        return redirect(url_for('efm_page',
                                message=result))

# TODO: Update insurance company
