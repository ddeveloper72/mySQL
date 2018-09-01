import os
import datetime
import pymysql.cursors

# Get username from Cloud9 workspace
# Modify this variable if running in another environment
username = os.getenv('C9_USER')

#c Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    # Run a query
    with connection.cursor() as cursor: # leaving the argument blank, returns list of tupls
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still dispaly a warning (not an error)
        # if the table already exists.
finally:
    # Close the connection, whether or not data has been returned
    connection.close()