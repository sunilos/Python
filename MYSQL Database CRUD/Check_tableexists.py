# Example to Check if table exists in  Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#to Check if table Exists in Database

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

mycursor = cnx.cursor()  
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)