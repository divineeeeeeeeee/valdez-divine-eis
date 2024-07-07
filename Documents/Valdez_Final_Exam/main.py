from flask import Flask, render_template, request, redirect, session
from users import Users 
from employees import Employee
from connector import Connector
from routes.dashboard_routes import dashboard_routes
from routes.add_employee_routes import add_employee_routes
from routes.employee_routes import employee_routes
from routes.add_new_employee_routes import add_employee_bp 
from routes.logout_routes import logout_routes
from routes.first_update_employee_routes import first_update_employee_routes
from routes.second_update_employee_routes import update_employee_routes
from routes.delete_employee_routes import delete_employee_routes


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'Roropaz08'  # Secret key for session management

app.register_blueprint(employee_routes, url_prefix='/employee')
app.register_blueprint(add_employee_routes, url_prefix='/add-employee')
app.register_blueprint(first_update_employee_routes, url_prefix='/first-update-employee')
app.register_blueprint(update_employee_routes)
app.register_blueprint(delete_employee_routes)
app.register_blueprint(dashboard_routes, url_prefix="/")
app.register_blueprint(add_employee_bp)
app.register_blueprint(logout_routes)

print(app.url_map)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form["username"]
    password = request.form["password"]

    result = Users.check_user(username, password)

    if result:
        return redirect('/dashboard')
    else:
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run(debug=True)
