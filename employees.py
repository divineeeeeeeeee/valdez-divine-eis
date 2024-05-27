from connector import Connector

class Employee:

    def get_all():
        query = "SELECT * FROM employees"

        cursor = Connector.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result