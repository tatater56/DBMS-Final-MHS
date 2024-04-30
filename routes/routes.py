from flask import render_template, url_for, redirect, request
from __main__ import app

import routes.employee_facility_routes
import routes.patient_management_routes
import routes.management_reporting_routes

@app.route('/')
def main_page():
    return render_template('MainMenu.html',
                            message = request.args.get("message", default = None))

@app.route('/api/CreateDB')
def api_create_db():
    db.create_db()
    return redirect(url_for('main_page', message='DB created'))

@app.route('/api/PopulateDB')
def api_populate_db():
    db.populate_db()
    return redirect(url_for('main_page', message='DB populated'))
