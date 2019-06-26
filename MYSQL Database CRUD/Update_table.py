# Example to Update Record in Table
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

my_cursor= conn.cursor()

#sql_update ="update student set StudentEmail='s@gmail.com' where StudentEmail = 'savita@nenosystems'"
conn.cursor().execute("update student set StudentEmail='a@gmail.com' where StudentEmail = 'aa@gmail.com'")
conn.commit()
print("One Record Updated")