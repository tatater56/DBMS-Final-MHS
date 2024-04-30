from flask import render_template, url_for, redirect, request
from __main__ import app

import database.employee as employee
import database.facility as facility
import database.db as db


# Main page

@app.route('/PatientManagement')
def pm_page():
    return render_template('PatientManagement.html',
                            message = request.args.get("message", default = None))


# New patient


# Update patient


# Delete patient


# New appointment


# Update appointment


# Delete appointment
