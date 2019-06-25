# Example to Drop Table from  Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Drop Table form Database
from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

mycursor= cnx.cursor()

sql_drop = "DROP TABLE registeration"

mycursor.execute(sql_drop)

print("Table is removed from Database")