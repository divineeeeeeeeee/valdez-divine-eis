from flask import Blueprint, render_template

dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")