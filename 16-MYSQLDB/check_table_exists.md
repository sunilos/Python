Here’s the code with comments added, followed by a brief explanation:

```python
# Example to Check if Table Exists in Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Import the connection object from the mysql.connector module
from mysql.connector import connection

# Establish a connection to the MySQL database
conn = connection.MySQLConnection(
    user='root',            # MySQL username
    password='root',        # MySQL password
    host='localhost',       # Database server address
    charset='utf8',         # Character set for encoding
    database='testdb'       # Name of the database to connect to
)

# Create a cursor object to interact with the database
my_cursor = conn.cursor()  

# Execute an SQL command to list all tables in the database
my_cursor.execute("SHOW TABLES")

# Iterate over the results and print each table name
for x in my_cursor:
    print(x)  # Each result is a tuple containing the table name
```

### Brief Explanation:

1. **Import Module**:
   - `from mysql.connector import connection`: Imports the `connection` object from the `mysql.connector` module to handle MySQL database connections.

2. **Establish Database Connection**:
   - `conn = connection.MySQLConnection(...)`: Creates a connection to the MySQL database using the provided credentials and connection details.
     - `user='root'`: Specifies the MySQL username.
     - `password='root'`: Specifies the MySQL password.
     - `host='localhost'`: Specifies the address of the database server (localhost means the database is on the same machine).
     - `charset='utf8'`: Sets the character encoding for the connection.
     - `database='testdb'`: Specifies the name of the database to connect to.

3. **Create Cursor**:
   - `my_cursor = conn.cursor()`: Creates a cursor object to interact with the database. The cursor is used to execute SQL queries and fetch results.

4. **Execute SQL Command**:
   - `my_cursor.execute("SHOW TABLES")`: Executes the SQL command `SHOW TABLES`, which retrieves the list of all tables in the connected database.

5. **Iterate and Print Tables**:
   - `for x in my_cursor:`: Iterates over the results returned by the `SHOW TABLES` command.
     - `print(x)`: Prints each table name. Each result is a tuple where the first element is the table name.

This code connects to a MySQL database and lists all the tables present in the specified database. The output will be a list of tuples, each containing the name of a table.