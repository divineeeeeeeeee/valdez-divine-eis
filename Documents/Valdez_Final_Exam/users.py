from connector import Connector

class Users:

    @staticmethod
    def check_user(username, password):
        query = "SELECT * FROM users WHERE username=%s AND password=%s"

        cursor = Connector.cursor()
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result is None:
            return False

        return True