from flask import Blueprint, render_template, redirect, request, session
from app.models.employees import Employee  # Adjust import as needed

# Create a Blueprint object
update_employee_routes = Blueprint("update_employee_routes", __name__)

@update_employee_routes.route('/employee-list')
def employee_list():
    employees = Employee.get_all()
    return render_template('employee_list.html', employees=employees)

@update_employee_routes.route('/update-employee', methods=['POST'])
def update_employee():
    emp_id = request.form.get("employee_id")
    lname = request.form.get("lname")
    fname = request.form.get("fname")
    mname = request.form.get("mname")

    # Call a method to add employee (assuming it's defined in Employee model)
    success = Employee.update_employee(emp_id, lname, fname, mname)

    if success:
        session["message"] = "Successfully Updated"
    else:
        session["message"] = "Failed to Update employee"

    return redirect('/employee-list')
