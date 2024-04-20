from flask import render_template
from __main__ import app

@app.route('/')
def main_page():
    return render_template('MainMenu.html')

@app.route('/EmployeeFacilityManagement')
def efm_page():
    return render_template('EmployeeFacilityManagement.html')

@app.route('/PatientManagement')
def pm_page():
    return render_template('PatientManagement.html')

@app.route('/ManagementReporting')
def mr_page():
    return render_template('ManagementReporting.html')
