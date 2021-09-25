import os
import pymysql
# Different from the video. The below import of MySQLdb is part of Scott Boning's recommended fix, and I will highlight 
# throughout this file where those other fixes have been used. 
import MySQLdb

# Get username from workspace
# username = os.getenv('USER_JAMES') <-- This is the original from the video, below is the fixed version
username = 'root'
# Below is the page you used to learn how to set up a new user and give yourself permission to use it
# https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                            port = 3306,
                            user = 'root',
                            password = '',
                            db = 'Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection regardless of whether the above was successful
    connection.close()

