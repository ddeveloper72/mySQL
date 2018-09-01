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
        list_of_names = ['fred', 'Fred']
        # Prepare a string withe same number of pace holders as in the list of names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({}); ".format(format_strings), list_of_names)
        
        connection.commit()
finally:
    # Close the connection, whether or not data has been returned
    connection.close()