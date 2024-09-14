Here's the code with added comments, followed by a brief explanation:

```python
# Example to Drop Table from Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Drop Table from Database
from mysql.connector import connection

# Establish a connection to the MySQL server and select the database
conn = connection.MySQLConnection(
    user='root',            # MySQL username
    password='root',        # MySQL password
    host='localhost',       # Database server address (localhost for local server)
    charset='utf8',         # Character set for encoding
    database='testdb'       # Name of the database to connect to
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute an SQL command to drop the 'registeration' table from the database
cursor.execute("DROP TABLE registeration")

# Print a confirmation message
print("Table is removed from Database")

# Close the cursor and connection
cursor.close()
conn.close()
```

### Brief Explanation:

1. **Import Module**:
   - `from mysql.connector import connection`: Imports the `connection` object from the `mysql.connector` module to manage connections to a MySQL database.

2. **Establish Database Connection**:
   - `conn = connection.MySQLConnection(...)`: Creates a connection to the MySQL server with the specified parameters.
     - `user='root'`: MySQL username.
     - `password='root'`: MySQL password.
     - `host='localhost'`: Host address of the MySQL server.
     - `charset='utf8'`: Character set to use for the connection.
     - `database='testdb'`: Database to connect to.

3. **Create Cursor Object**:
   - `cursor = conn.cursor()`: Creates a cursor object to execute SQL commands.

4. **Drop Table**:
   - `cursor.execute("DROP TABLE registeration")`: Executes an SQL command to drop (delete) the `registeration` table from the database.

5. **Print Confirmation**:
   - `print("Table is removed from Database")`: Prints a confirmation message indicating that the table has been removed.

6. **Close Resources**:
   - `cursor.close()`: Closes the cursor object to free up database resources.
   - `conn.close()`: Closes the connection to the MySQL server.