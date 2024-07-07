from flask import Blueprint, render_template, redirect, request, session
from app.models.employees import Employee

# Create a Blueprint object
delete_employee_routes = Blueprint("delete_employee_routes", __name__)

@delete_employee_routes.route('/employee-list')
def employee_list():
    employees = Employee.get_all()
    return render_template('employee_list.html', employees=employees)

@delete_employee_routes.route('/delete-employee/<int:employee_id>', methods=['GET', 'POST'])
def delete_employee(employee_id):
    employees = Employee.delete_employee(employee_id)
    if True:
        session["message"] = "Successfully Deleted."
        return redirect('/employee-list')
    else:
        session["message"] = "Employee not found."
        return redirect('/employee-list')