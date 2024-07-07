from flask import Blueprint, render_template, request, redirect, session
from app.models.employees import Employee  # Adjust this import based on your actual project structure

# Assuming this Blueprint is registered with your Flask app elsewhere
add_employee_bp = Blueprint('add_employee_bp', __name__)

@add_employee_bp.route('/employee-list')
def employee_list():
    employees = Employee.get_all()
    return render_template('employee_list.html', employees=employees)

@add_employee_bp.route('/add-new-employee', methods=['POST'])
def add_new_employee():
    emp_id = request.form.get("emp_id")
    lname = request.form.get("lname")
    fname = request.form.get("fname")
    mname = request.form.get("mname")

    # Call a method to add employee (assuming it's defined in Employee model)
    success = Employee.add_employee(emp_id, lname, fname, mname)

    if success:
        session["message"] = "Successfully Added"
    else:
        session["message"] = "Failed to add employee"

    return redirect('/employee-list')
