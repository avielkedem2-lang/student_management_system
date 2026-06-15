import mysql.connector


class DBConnector:
    def __init__(self):
        self.config = {
            "host":"127.0.0.1",
            "port": "3306",
            "password":"4321",
            "database":"students_db"
        }
        self.connection = None
        self.cusor = None
    
    def connect(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(dictionary=True)

