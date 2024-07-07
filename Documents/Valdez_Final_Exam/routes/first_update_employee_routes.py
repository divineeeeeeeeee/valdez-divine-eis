from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models.employees import Employee  # Assuming this is your Employee model

first_update_employee_routes = Blueprint("first_update_employee_routes", __name__)

@first_update_employee_routes.route('/employee-list')
def employee_list():
    employees = Employee.get_all()
    return render_template('employee_list.html', employees=employees)

@first_update_employee_routes.route('/first-update-employee/<int:employee_id>', methods=['GET', 'POST'])
def first_update_employee(employee_id):
    employees = Employee.get_employee(employee_id)
    if employees:
        return render_template('update_employees.html', employees=employees, employee_id=employee_id)
    else:
        session["message"] = "Employee not found."
        return redirect('/employee-list')