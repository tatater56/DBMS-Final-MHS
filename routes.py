from flask import render_template, url_for, redirect, request
from __main__ import app

import database.employee as employee
import database.db as db

from typing import Optional

### Main menu ###

@app.route('/')
def main_page():
    return render_template('MainMenu.html',
                            message = request.args.get("message", default = None))


### Employee ###

@app.route('/EmployeeFacilityManagement')
def efm_page():
    return render_template('EmployeeFacilityManagement.html',
                            message = request.args.get("message", default = None),
                            employees = employee.get_all())

@app.route('/NewEmployee/<JobClass>')
def new_employee_page(JobClass):
    return render_template('employee/new.html', JobClass=JobClass)

@app.route('/api/NewEmployee')
def api_new_employee():
    return redirect(url_for('efm_page', message='New employee created'))

@app.route('/UpdateEmployee/<EmpID>')
def update_employee_page(EmpID):
    return render_template('employee/update.html', employee=employee.get(EmpID))

@app.route('/api/UpdateEmployee')
def api_update_employee():
    return redirect(url_for('efm_page', message='Employee updated'))

@app.route('/DeleteEmployee/<EmpID>')
def delete_employee_page(EmpID):
    return render_template('employee/delete.html', employee=employee.get(EmpID))

@app.route('/api/DeleteEmployee')
def api_delete_employee():
    return redirect(url_for('efm_page', message='Employee deleted'))



### Patient pages ###

@app.route('/PatientManagement')
def pm_page():
    return render_template('PatientManagement.html',
                            message = request.args.get("message", default = None))


### Management pages ###

@app.route('/ManagementReporting')
def mr_page():
    return render_template('ManagementReporting.html',
                            message = request.args.get("message", default = None))


### DB ###

@app.route('/api/CreateDB')
def api_create_db():
    db.create_db()
    return redirect(url_for('main_page', message='DB created'))

@app.route('/api/PopulateDB')
def api_populate_db():
    db.populate_db()
    return redirect(url_for('main_page', message='DB populated'))

