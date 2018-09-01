import os
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
        rows = [(23, "Bob"),
                (24, "Jim"),
                (25, "Fred")]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                        rows)
        
        connection.commit()
finally:
    # Close the connection, whether or not data has been returned
    connection.close()