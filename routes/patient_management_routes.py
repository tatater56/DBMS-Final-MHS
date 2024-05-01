from flask import render_template, url_for, redirect, request
from __main__ import app

from database import db, employee, facility, insurance, patient, appointment
import util

# Main page

@app.route('/PatientManagement')
def pm_page():
    return render_template('PatientManagement.html',
                            message = request.args.get("message", default = None),
                            patients = patient.get_all(),
                            appointments = appointment.get_all())


# New patient

@app.route('/NewPatient')
def new_patient_page():
    return render_template('patient/new.html',
                            insurances = insurance.get_all(),
                            doctors = employee.get_all_doctors_with_names())

@app.route('/api/NewPatient', methods=['POST'])
def api_new_patient():
    form_dict = {k: v for k, v in request.form.items()}

    result = patient.create(form_dict)
    if(result):
        message = f'New patient created (id:{result})'
    else:
        message = 'Error encountered while attempting to create patient!'

    return redirect(url_for('pm_page', 
                        message=message))

# Delete patient

@app.route('/api/DeletePatient/<P_id>')
def api_delete_patient(P_id):
    if(util.is_empty_string(P_id)):
        return redirect(url_for('pm_page',
                                message='Patient could not be deleted, no P_id given'))
    else:
        result = ''
        if patient.delete(P_id):
            result = f'Patient deleted (id:{P_id})'
        else:
            result = f'Error encountered, could not delete patient (id:{P_id})'
        
        return redirect(url_for('pm_page',
                                message=result))

# TODO: Update patient


@app.route('/NewAppointment')
def new_appointment_page():
    return render_template('appointment/new.html',
                            doctors = employee.get_all_doctors_with_names(),
                            patients = patient.get_all(),
                            facilities = facility.get_all())

@app.route('/api/NewAppointment', methods=['POST'])
def api_new_appointment():
    form_dict = {k: v for k, v in request.form.items()}

    result = appointment.create(form_dict)
    if(result):
        message = f'New appointment created (id:{result})'
    else:
        message = 'Error encountered while attempting to create appointment!'

    return redirect(url_for('pm_page', 
                        message=message))


# Update appointment

@app.route('/UpdateAppointment/<AppID>')
def update_appointment_page(AppID):
    return render_template('appointment/update.html',
                            appointment = appointment.get(AppID),
                            doctors = employee.get_all_doctors_with_names(),
                            patients = patient.get_all(),
                            facilities = facility.get_all())

@app.route('/api/UpdateAppointment', methods=['POST'])
def api_update_appointment():
    form_dict = {k: v for k, v in request.form.items()}
    AppID = appointment.update(form_dict)

    if AppID:
        result = f"Appointment updated (id:{AppID})"
    else:
        result = "Could not update appointment"

    return redirect(url_for('pm_page',
                            message=result))

# Delete appointment
@app.route('/api/DeleteAppointment/<AppID>')
def api_delete_appointment(AppID):
    if(util.is_empty_string(AppID)):
        return redirect(url_for('pm_page',
                                message='Appointment could not be deleted, no AppID given'))
    else:
        result = ''
        if appointment.delete(AppID):
            result = f'Appointment deleted (id:{AppID})'
        else:
            result = f'Error encountered, could not delete Appointment (id:{AppID})'
        
        return redirect(url_for('pm_page',
                                message=result))
