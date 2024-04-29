from flask import render_template, url_for, redirect, request
from __main__ import app

import database.employee as employee
import database.db as db

from typing import Optional

### Menus ###

@app.route('/')
def main_page():
    return render_template('MainMenu.html',
                            message = request.args.get("message", default = None))

@app.route('/EmployeeFacilityManagement')
def efm_page():
    return render_template('EmployeeFacilityManagement.html',
                            message = request.args.get("message", default = None),
                            employees = employee.get_all())

@app.route('/PatientManagement')
def pm_page():
    return render_template('PatientManagement.html',
                            message = request.args.get("message", default = None))

@app.route('/ManagementReporting')
def mr_page():
    return render_template('ManagementReporting.html',
                            message = request.args.get("message", default = None))

### API ###

@app.route('/api/CreateDB')
def api_create_db():
    db.create_db()
    return redirect(url_for('main_page', message='DB created'))

@app.route('/api/PopulateDB')
def api_populate_db():
    db.populate_db()
    return redirect(url_for('main_page', message='DB populated'))

