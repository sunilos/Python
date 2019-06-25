# Example to Insert multiple records in table 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 
#Insert Multiple Records in table

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

sql_multiple ="insert into student(Studentname,RollNo,StudentEmail)values(%s,%s,%s)"
val=[
  ('Peter', '0206cs122','a@gmail.com'),
  ('Amy', '0206cs125','b@gmail.com'),
  ('Hannah', '0206cs126','c@gmail.com'),
  ('Michael', '0206cs127','d@gmail.com'),
  ('Sandy', '0206cs128','e@gmail.com'),
  ('Viola', '0206cs129','f@gmail.com')
]
mycursor = cnx.cursor()
mycursor.executemany(sql_multiple, val)
cnx.commit()
print("Multiple Successfully Inserted")
cnx.close()