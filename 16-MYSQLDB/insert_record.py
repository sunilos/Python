# Example of Insert Record in Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Insert Data into  table

from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')
    
#To Insert Single record in table
sql_insert = "Insert into student(Studentname,RollNo,StudentEmail)values('John','0206ca121','john@gmail.com')"
my_cursor = conn.cursor()
my_cursor.execute(sql_insert)
conn.commit()
print("Data Successfully Inserted")
conn.close()

