# Example to Create  table in Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

#Create table using Python Functions

from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

conn.cursor().execute("create table student(sid int primary key auto_increment, StudentName VARCHAR(255),RollNo VARCHAR(255))")

conn.cursor().execute("CREATE TABLE Registeration (regid int primary key auto_increment, Firstname VARCHAR(255),LastName VARCHAR(255),Email VARCHAR(255),Password VARCHAR(255),MobileNumber VARCHAR(255), address VARCHAR(255))")
