from flask import Blueprint, render_template, request, redirect, session
from app.models.employees import Employee

employee_routes = Blueprint("employee_routes", __name__)

@employee_routes.route('/employee-list')
def employee_list():
    employees = Employee.get_all()
    return render_template('employee_list.html', employees=employees)
