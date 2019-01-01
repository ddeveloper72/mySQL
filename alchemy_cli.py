import os
import pymysql.cursors


# Get username from Heroku workspace
# Modify this variable if running in another environment

                       
connection = pymysql.connect('eu-cdbr-west-02.cleardb.net','be6fbfb767ab56','f3491c52','heroku_5743e02b43306cc')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql='SELECT * FROM Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, whether or not data has been returned
    connection.close()