# Example of Fetch All record From Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Fetch  Data form table and show 

from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

my_cursor = conn.cursor()
my_cursor.execute("select * from student")
my_result = my_cursor.fetchall() #fetchall() method fetch all rows from executed query 
print("Data Listed Below:")

for x in my_result:
    print(x)

