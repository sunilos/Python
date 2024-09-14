Here's the code with comments added, followed by a brief explanation:

```python
# Example to Create Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Import the connection object from the mysql.connector module
from mysql.connector import connection

# Establish a connection to the MySQL server
conn = connection.MySQLConnection(
    user='root',            # MySQL username
    password='root',        # MySQL password
    host='localhost',       # Database server address (localhost for local server)
    charset='utf8',         # Character set for encoding
    database='testdb'       # Name of the database to connect to
)

# Print the connection object to confirm successful connection
print(conn)
```

### Brief Explanation:

1. **Import Module**:
   - `from mysql.connector import connection`: Imports the `connection` object from the `mysql.connector` module to manage connections to a MySQL database.

2. **Establish Database Connection**:
   - `conn = connection.MySQLConnection(...)`: Creates a connection to the MySQL server with the specified parameters.
     - `user='root'`: Specifies the username for the MySQL server.
     - `password='root'`: Specifies the password associated with the MySQL username.
     - `host='localhost'`: Specifies the host address of the MySQL server (localhost means the server is on the same machine).
     - `charset='utf8'`: Specifies the character set to use for the connection.
     - `database='testdb'`: Specifies the database to connect to upon establishing the connection.

3. **Print Connection Object**:
   - `print(conn)`: Prints the connection object to confirm that the connection has been successfully established. If the connection is successful, this will print a representation of the connection object.

**Note:** The code as provided does not actually create a new database. It connects to an existing database named `'testdb'`. If you need to create a database, you would typically execute an SQL command like `CREATE DATABASE` using a cursor object. For example:

```python
# Create a cursor object
cursor = conn.cursor()

# Execute the SQL command to create a new database
cursor.execute("CREATE DATABASE new_database_name")

# Close the cursor and connection
cursor.close()
conn.close()
```