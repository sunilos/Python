
# Example to fetch record from table using Orderby Clause
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

mycursor= cnx.cursor()

sql_fetch = "SELECT * FROM student ORDER BY RollNo DESC"

mycursor.execute(sql_fetch)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)