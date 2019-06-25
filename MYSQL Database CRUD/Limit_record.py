# Example to show limited records using limit Clause
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Example  to show Limited Record by limit Clause 
from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

mycursor= cnx.cursor()
mycursor.execute("SELECT * FROM student LIMIT 4")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)