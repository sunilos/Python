#Delete Data From table By Id 
# Example to Delete Record from Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  
from mysql.connector import (connection)

conn = connection.MySQLConnection(user='root',
    password='root', 
    host='localhost', 
    charset='utf8', 
    database='testdb')

conn.cursor().execute("DELETE FROM student WHERE sid = '1'")
conn.commit()
print("One record Deleted")