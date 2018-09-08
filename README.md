# MySQL, It's all about Data on Cloud 9 in...
# Data Centric Development


Welcome to my Python project on Cloud9 IDE!  Yes I've taken over the default Readme
to add in a few more bits about what this [Code Institute](https://courses.codeinstitute.net/) tutorial was all about.

This tutoral focused on learning the essential [MySQL](https://www.mysql.com/) commands.

The Learning Outcomes Are:

* Connecting to MySQL from Python,
* Queries and cursors,
* Query the database with select,
* Updating, inserting,
* Deleting,
* Cursors,
* Creating tables and inserting data,
* Updating data,
* Deleting data and loading data into a dictionary


1 Running MySQL on Cloud9

* Installing MySQL:

```
sudo pip3 install setuptools --upgrade && sudo pip3 install pip --upgrade && sudo pip3 install pymysql
```

* Starting MySQL from the command line:

```
sudo service mysql start
```

or

```
mysql-ctl start
```

To connect to mysql: 

```
	mysql -u $C9_USER -p
```

* Switching to a database:

```
	USE DatabaseName
```

## The Results!

The app was run from Cloud9

1 To connect to mysql & select the tutorial database: 

```python
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
```

2 Sample code where the age of a candidate is updated:

```python
try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                        (23, "Bob"))
        
        connection.commit()
finally:
    # Close the connection, whether or not data has been returned
    connection.close()
```

