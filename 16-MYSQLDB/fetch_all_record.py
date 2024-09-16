
# Example to fetch record from table using Orderby Clause
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

my_cursor= conn.cursor()
sql_fetch = "SELECT * FROM student ORDER BY RollNo DESC"
my_cursor.execute(sql_fetch)
my_result = my_cursor.fetchall()

for x in my_result:
  print(x)
