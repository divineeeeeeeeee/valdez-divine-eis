from flask import Blueprint, render_template

add_employee_routes = Blueprint("add_employee_routes", __name__)

@add_employee_routes.route("/add-employee")
def add_employee():
    return render_template("add_employee.html")

