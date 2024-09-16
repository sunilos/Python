```python
# Example to fetch records from a table using ORDER BY clause
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Importing the necessary module from MySQL Connector package to establish a database connection
from mysql.connector import (connection)

# Establishing the connection to the MySQL database with the necessary credentials
# 'user', 'password', 'host', 'charset', and 'database' parameters are provided to connect
conn = connection.MySQLConnection(user='root', 
    password='root',  # Database password
    host='localhost',  # Database host, here it's the local machine
    charset='utf8',  # Character set to support UTF-8 encoding for multilingual data
    database='testdb')  # The name of the database to connect to

# Creating a cursor object using the connection, which will be used to execute SQL queries
my_cursor = conn.cursor()

# Defining an SQL query to fetch all records from the 'student' table and order them by 'RollNo' in descending order
sql_fetch = "SELECT * FROM student ORDER BY RollNo DESC"

# Executing the SQL query using the cursor object
my_cursor.execute(sql_fetch)

# Fetching all the rows returned by the executed query
my_result = my_cursor.fetchall()

# Looping through the result set and printing each row (record) one by one
for x in my_result:
  print(x)  # Each 'x' represents a tuple containing the values of a row
```

### Explanation:

1. **Importing the `connection` module**:
   - This imports the required functionality to connect to a MySQL database using the MySQL Connector package.

2. **Establishing Connection**:
   - A connection object `conn` is created using the `MySQLConnection` method with arguments like `user`, `password`, `host`, `charset`, and `database`. These parameters are used to connect to the MySQL database (`testdb`).

3. **Creating a Cursor Object**:
   - A cursor `my_cursor` is created from the connection object. This cursor will be used to interact with the database by executing SQL queries.

4. **SQL Query Definition**:
   - The SQL query `"SELECT * FROM student ORDER BY RollNo DESC"` is defined. It selects all records from the `student` table and orders them in descending order based on the `RollNo` field.

5. **Executing the SQL Query**:
   - The `execute()` method of the cursor is used to execute the SQL query. It sends the query to the database and prepares the result set for fetching.

6. **Fetching Results**:
   - The `fetchall()` method fetches all the rows returned by the query execution. The result is stored in `my_result`, which is a list of tuples where each tuple represents a row from the table.

7. **Looping through Results**:
   - A `for` loop is used to iterate through the result set (`my_result`). Each record (a tuple) is printed to the console.

