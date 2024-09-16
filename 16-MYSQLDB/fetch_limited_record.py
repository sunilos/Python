# Example to show limited records using limit Clause
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Example  to show Limited Record by limit Clause 
from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

my_cursor= conn.cursor()
my_cursor.execute("SELECT * FROM student LIMIT 4")
my_result = my_cursor.fetchall()

for x in my_result:
  print(x)
