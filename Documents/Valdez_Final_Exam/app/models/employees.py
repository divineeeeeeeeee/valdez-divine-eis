from connector import Connector

class Employee:

    @staticmethod
    def get_all():
        query = "SELECT * FROM employees"
        with Connector.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result

    @staticmethod
    def add_employee(emp_id, lname, fname, mname):
        query = "INSERT INTO employees VALUES (%s, %s, %s, %s)"
        try:
            with Connector.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (emp_id, lname, fname, mname))
                    conn.commit()
            return True
        except Exception as e:
            print(f"Error in add_employee: {e}")
            return False

    @staticmethod
    def get_employee(emp_id):
        query = "SELECT * FROM employees WHERE employee_id = %s"
        try:
            with Connector.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (emp_id,))
                    result = cursor.fetchall()
            if result:
                return result
            else:
                return None
        except Exception as e:
            print(f"Error in get_employee: {e}")
            return None
                
    @staticmethod
    def update_employee(employee_id, lname, fname, mname):
        query = "UPDATE employees SET lname = %s, fname = %s, mname = %s WHERE employee_id = %s"
        try:
            with Connector.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (lname, fname, mname, employee_id))
                    conn.commit()
            return True
        except Exception as e:
            print(f"Error in update_employee: {e}")
            return False


    @staticmethod
    def delete_employee(emp_id):
        query = "DELETE FROM employees WHERE employee_id = %s"
        try:
            with Connector.get_connection() as conn:
                with conn.cursor() as cursor:
                    rows_affected = cursor.execute(query, (emp_id,))
                    conn.commit()
            if rows_affected > 0:
                print(f"Employee {emp_id} deleted successfully")
                return True
            else:
                print(f"No employee found with ID {emp_id}")
                return False
        except Exception as e:
            print(f"Error in delete_employee: {e}")
            return False