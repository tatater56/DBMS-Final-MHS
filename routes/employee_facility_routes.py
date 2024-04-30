from flask import render_template, url_for, redirect, request
from __main__ import app

import database.employee as employee
import database.facility as facility
import database.db as db


# Main page

@app.route('/EmployeeFacilityManagement')
def efm_page():
    return render_template('EmployeeFacilityManagement.html',
                            message = request.args.get("message", default = None),
                            employees = employee.get_all())


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
        return redirect(url_for('efm_page', 
                                message=f'New employee created (id:{result})'))
    else:
        return redirect(url_for('efm_page',
                                message='Error encountered while attempting to create empployee!'))


# Update employee

@app.route('/UpdateEmployee/<EmpID>')
def update_employee_page(EmpID):
    return render_template('employee/update.html',
                            employee=employee.get(EmpID))

@app.route('/api/UpdateEmployee', methods=['POST'])
def api_update_employee():
    return redirect(url_for('efm_page',
                            message='Employee updated'))


# Delete employee

@app.route('/DeleteEmployee/<EmpID>')
def delete_employee_page(EmpID):
    return render_template('employee/delete.html',
                            employee=employee.get(EmpID))

@app.route('/api/DeleteEmployee/<EmpID>')
def api_delete_employee(EmpID):
    if(EmpID):
        result = employee.delete(EmpID)
        return redirect(url_for('efm_page',
                                message='Employee deleted'))
    else:
        return redirect(url_for('efm_page',
                                message='Employee could not be deleted, no EmpID given'))


# TODO: facilities
