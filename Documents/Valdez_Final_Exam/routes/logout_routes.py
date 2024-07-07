from flask import Blueprint, render_template, redirect, request, url_for
from users import Users  # Assuming Users is correctly imported and defined

logout_routes = Blueprint("logout_routes", __name__)

@logout_routes.route("/logout")
def logout():
    # Redirect to the login route using url_for to ensure correct URL resolution
    return render_template('login.html')

@logout_routes.route('/dashboard')
def dashboard():
    # Placeholder function to render the dashboard template
    return render_template('dashboard.html')

@logout_routes.route('/check-user', methods=['POST'])
def check_user():
    # Retrieve username and password from the form
    username = request.form["username"]
    password = request.form["password"]

    # Check if the user credentials are valid using the Users class
    result = Users.check_user(username, password)

    # Redirect to the dashboard if credentials are valid, otherwise render the login page again
    if result:
        return redirect(url_for('logout_routes.dashboard'))  # Redirect using url_for to ensure correct URL resolution
    else:
        return render_template('login.html')
