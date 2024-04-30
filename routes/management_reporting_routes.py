from flask import render_template, url_for, redirect, request
from __main__ import app

import database.employee as employee
import database.facility as facility
import database.db as db


# Main page

@app.route('/ManagementReporting')
def mr_page():
    return render_template('ManagementReporting.html',
                            message = request.args.get("message", default = None))

