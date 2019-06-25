# Example of Fetch All record From Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Fetch  Data form table and show 

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

mycursor = cnx.cursor()
mycursor.execute("select * from student")

result = mycursor.fetchall() #fetchall() method fetch all rows from executed query 
print("Data Listed Below:")
for x in result:
    print(x)