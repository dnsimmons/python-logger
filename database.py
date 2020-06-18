import mysql.connector

# Database config
config = {
    'host': 'localhost',
    'user': 'dsimmons',
    'password': 'test',
    'database': 'laravel'
}

# Database class
class Database:

    # Class constructor
    def __init__(self):
        self.connect()

    # Connect to the database
    def connect(self):
        try:
            self.db = mysql.connector.connect(**config)
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            print(err.msg)
            return False