Here's the code with added comments and a brief explanation:

```python
# Example of Fetch All Records From Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Fetch Data from table and show

from mysql.connector import connection

# Establish a connection to the MySQL server and select the database
conn = connection.MySQLConnection(
    user='root',            # MySQL username
    password='root',        # MySQL password
    host='localhost',       # Database server address (localhost for local server)
    charset='utf8',         # Character set for encoding
    database='testdb'       # Name of the database to connect to
)

# Create a cursor object to interact with the database
my_cursor = conn.cursor()

# Execute SQL query to select all records from the 'student' table
my_cursor.execute("SELECT * FROM student")

# Fetch all rows from the executed query
my_result = my_cursor.fetchall()

# Print a header for the output
print("Data Listed Below:")

# Iterate over the fetched results and print each record
for x in my_result:
    print(x)

# Close the connection to the MySQL server
conn.close()
```

### Brief Explanation:

1. **Import Module**:
   - `from mysql.connector import connection`: Imports the `connection` object from the `mysql.connector` module to manage MySQL database connections.

2. **Establish Database Connection**:
   - `conn = connection.MySQLConnection(...)`: Creates a connection to the MySQL server with specified parameters:
     - `user='root'`: MySQL username.
     - `password='root'`: MySQL password.
     - `host='localhost'`: Host address of the MySQL server.
     - `charset='utf8'`: Character set for the connection.
     - `database='testdb'`: Database to connect to.

3. **Create Cursor Object**:
   - `my_cursor = conn.cursor()`: Creates a cursor object to execute SQL queries and interact with the database.

4. **Execute SQL Query**:
   - `my_cursor.execute("SELECT * FROM student")`: Executes an SQL query to select all records from the `student` table.

5. **Fetch All Records**:
   - `my_result = my_cursor.fetchall()`: Fetches all rows from the executed query and stores them in `my_result`. The `fetchall()` method retrieves all the rows of the query result.

6. **Print Header**:
   - `print("Data Listed Below:")`: Prints a header to indicate that the following output will list the data fetched from the table.

7. **Print Results**:
   - `for x in my_result: print(x)`: Iterates over the fetched records and prints each record.

8. **Close Connection**:
   - `conn.close()`: Closes the connection to the MySQL server to free up resources.
