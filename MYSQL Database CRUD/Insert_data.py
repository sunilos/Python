# Example of Insert Record in Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Insert Data into  table

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')
#To Insert Single record in table
sqlinsert = "Insert into student(Studentname,RollNo,StudentEmail)values('John','0206ca121','john@gmail.com')"
mycursor = cnx.cursor()
mycursor.execute(sqlinsert)
cnx.commit()
print("Data Successfully Inserted")
cnx.close()