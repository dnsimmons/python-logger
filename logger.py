import mysql.connector
import datetime
from database import Database


# Logger class extends database class
class Logger(Database):

    # Class constructor
    def __init__(self):
        super().__init__()

    # Fetch log records
    def get_rows(self):
        try:
            sql = "SELECT * FROM logs ORDER BY log_date DESC"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Fetch a log record
    def get_row(self, id_record):
        try:
            sql = "SELECT * FROM logs WHERE id = %s"
            self.cursor.execute(sql, id_record)
            result = self.cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Store a log record
    def do_store(self, message):
        try:
            date = datetime.datetime.now()
            sql = "INSERT INTO logs (log_date, log_message) VALUES (%s, %s)"
            self.cursor.execute(sql, (date, message))
            self.cursor.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Update a log record
    def do_update(self, id_update, message):
        try:
            sql = "UPDATE logs SET log_message = %s WHERE id = %s"
            self.cursor.execute(sql, (message, id_update))
            self.cursor.commit()
            return True
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Delete a log record
    def do_destroy(self, id_destroy):
        try:
            sql = "DELETE FROM logs WHERE id = %s"
            self.cursor.execute(sql, id_destroy)
            self.cursor.commit()
            return True
        except mysql.connector.Error as err:
            print(err.msg)
            return False


obj = Logger()
data = obj.get_row(2)
