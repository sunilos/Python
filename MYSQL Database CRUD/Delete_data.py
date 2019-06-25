#Delete Data From table By Id 
# Example to Delete Record from Table
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
mycursor = cnx.cursor()

sql_delete = "DELETE FROM student WHERE sid = '3'"

mycursor.execute(sql_delete)

cnx.commit()
print("One record Deleted")