import mysql.connector

class Connector:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None or cls._connection.is_connected() is False:
            cls._connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="employee_information_system"
            )
        return cls._connection

    @classmethod
    def cursor(cls):
        return cls.get_connection().cursor()

    @classmethod
    def commit(cls):
        cls.get_connection().commit()

    @classmethod
    def rollback(cls):
        cls.get_connection().rollback()

    @classmethod
    def close(cls):
        if cls._connection is not None and cls._connection.is_connected():
            cls._connection.close()
            cls._connection = None