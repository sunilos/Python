# Example to Alter Table from  Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

mycursor = cnx.cursor()

mycursor.execute("ALTER TABLE student ADD COLUMN StudentEmail VARCHAR(255)")