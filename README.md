# python-logger
Simple MySQL logger CRUD  in Python 3

### Dependencies

    $ pip3 install mysql-connector-python
    $ pip3 install python-dotenv

### Configure

Create a .env file in your project directory to hold your database config:

    DB_HOSTNAME="localhost"
    DB_USERNAME="your-username"
    DB_PASSWORD="your-password"
    DB_DATABASE="your-database"
    
### Usage

    $ python3 logger.py
 
### Examples
    
    obj = Logger()

    # fetch all rows
    data = obj.get_rows()

    # fetch a row by ID
    data = obj.get_row(2)

    # store a row
    obj.do_store('this is a log entry!)

    # update a row by ID
    obj.do_store(2, 'this is a updated log entry!)

    # destroy a row by ID
    obj.do_destroy(2)

