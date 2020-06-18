import os
import mysql.connector
from dotenv import load_dotenv

# Load environment vars
load_dotenv()

# Database config
config = {
    'host': os.getenv("DB_HOSTNAME"),
    'user': os.getenv("DB_USERNAME"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_DATABASE")
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
            exit(1)