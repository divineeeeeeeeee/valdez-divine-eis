from connector import Connector
import traceback

class Employee:

    @staticmethod
    def get_all():
        query = "SELECT * FROM employees"

        cursor = Connector.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    
    @staticmethod
    def add_employee(emp_id, lname, fname, mname):
        query = "INSERT INTO employees VALUES (%s, %s, %s, %s)"
        
        try:
            cursor = Connector.cursor()
            cursor.execute(query, (emp_id, lname, fname, mname))
            Connector.db.commit()
            
            return True 
        except:
            return False

    @staticmethod
    def get_employee(emp_id):
        query = "SELECT * FROM employees WHERE employee_id = %s"
        try:
            cursor = Connector.cursor()
            cursor.execute(query, (emp_id,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error in get_employee: {e}")

    @staticmethod
    def update_employee(emp_id, lname, fname, mname):
        query = "UPDATE employees SET lname = %s, fname = %s, mname = %s WHERE employee_id = %s"
        try:
            Connector.cursor.execute(query, (lname, fname, mname, emp_id))
            Connector.db.commit()
            print(f"Employee {emp_id} updated successfully")
            return True
        except Exception as e:
            print(f"Error in update_employee: {e}")
            return False




    @staticmethod
    def delete_employee(emp_id):
        query = "DELETE FROM employees WHERE employee_id = %s"
        try:
            Connector.cursor.execute(query, (emp_id,))
            Connector.db.commit()
            print(f"Employee {emp_id} deleted successfully")
            return True
        except Exception as e:
            print(f"Error in delete_employee: {e}")
            return False

