# Example to fetch  selected  Record  from table  using Like keyword
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#Fetch   Data from table using like keyword

from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

sql_fetch = "SELECT  RollNo FROM student WHERE RollNo Like '%cs%'"
my_cursor = conn.cursor()
my_cursor.execute(sql_fetch)
my_result = my_cursor.fetchall()

for x in my_result:
  print(x)
