# Example to Update Record in Table
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

sql_update ="update student set StudentEmail='s@gmail.com' where StudentEmail = 'savita@nenosystems'"
mycursor.execute(sql_update)

cnx.commit()
print("One record updated")