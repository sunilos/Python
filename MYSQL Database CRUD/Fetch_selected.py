# Example to fetch  selected  Record  from table  using Like keyword
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#Fetch   Data from table using like keyword

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

sql_fetch = "SELECT * FROM student WHERE RollNo Like '%ca%'"
mycursor = cnx.cursor()
mycursor.execute(sql_fetch)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
