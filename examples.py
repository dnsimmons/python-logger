import mysql.connector
import datetime
from database import Database
#from database import db, cursor

# Logger class extends database class
class Logger(Database):

    # Class constructor
    def __init__(self):
        super().__init__()

    # Fetch log records
    def get_rows(self):
        try:
            sql = ("SELECT * FROM logs ORDER BY log_date DESC")
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Fetch a log record
    def get_row(self, id):
        try:
            sql = ("SELECT * FROM kb_articles WHERE id = %s")
            self.cursor.execute(sql, (id,))
            result = self.cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Store a log record
    def do_store(self, message):
        try:
            date = datetime.datetime.now()
            sql = ("INSERT INTO logs (log_date, log_message) VALUES (%s, %s)")
            cursor.execute(sql, (date, message))
            cursor.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Update a log record
    def do_update(self, id, message):
        try:
            sql = ("UPDATE logs SET log_message = %s WHERE id = %s")
            cursor.execute(sql, (message, id))
            cursor.commit()
            return True
        except mysql.connector.Error as err:
            print(err.msg)
            return False

    # Delete a log record
    def do_destroy(self, id):
        try:
            sql = ("DELETE FROM logs WHERE id = %s")
            cursor.execute(sql, (id,))
            cursor.commit()
            return True
        except mysql.connector.Error as err:
            print(err.msg)
            return False

obj = Logger()

data = obj.get_row(2)