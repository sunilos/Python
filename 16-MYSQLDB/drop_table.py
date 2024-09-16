# Example to Drop Table from  Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Drop Table form Database
from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

conn.cursor().execute("DROP TABLE registeration")
print("Table is removed from Database")
