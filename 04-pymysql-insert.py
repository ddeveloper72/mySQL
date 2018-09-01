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
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    # Close the connection, whether or not data has been returned
    connection.close()