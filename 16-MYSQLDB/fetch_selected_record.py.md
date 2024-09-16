Here's the code with added comments, followed by a brief explanation:

```python
# Example to fetch selected record column-wise from table using LIKE keyword
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

# Fetch data from the table using LIKE keyword
from mysql.connector import connection

# Establish a connection to the MySQL server and select the database
conn = connection.MySQLConnection(
    user='root',            # MySQL username
    password='root',        # MySQL password
    host='localhost',       # Database server address (localhost for local server)
    charset='utf8',         # Character set for encoding
    database='testdb'       # Name of the database to connect to
)

# SQL query to fetch 'RollNo' from the 'student' table where 'RollNo' contains 'cs'
sql_fetch = "SELECT RollNo FROM student WHERE RollNo LIKE '%cs%'"

# Create a cursor object to execute SQL queries
my_cursor = conn.cursor()

# Execute the SQL query
my_cursor.execute(sql_fetch)

# Fetch all records from the executed query
my_result = my_cursor.fetchall()  # This will fetch the records where 'RollNo' contains the substring 'cs'

# Iterate through the fetched records and print each 'RollNo'
for x in my_result:
    print(x)

# Close the cursor and connection
my_cursor.close()
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

3. **Define SQL Query**:
   - `sql_fetch = "SELECT RollNo FROM student WHERE RollNo LIKE '%cs%'"`: Defines an SQL query to select the `RollNo` column from the `student` table where the `RollNo` contains the substring `'cs'`.
     - `LIKE '%cs%'`: The `LIKE` keyword is used for pattern matching. `%` is a wildcard that matches zero or more characters, so `%cs%` matches any `RollNo` containing `'cs'`.

4. **Create Cursor Object**:
   - `my_cursor = conn.cursor()`: Creates a cursor object to execute SQL commands.

5. **Execute SQL Query**:
   - `my_cursor.execute(sql_fetch)`: Executes the SQL query defined above.

6. **Fetch Results**:
   - `my_result = my_cursor.fetchall()`: Fetches all records returned by the executed query (i.e., `RollNo` values that contain `'cs'`).

7. **Print Results**:
   - `for x in my_result: print(x)`: Iterates through the fetched records and prints each `RollNo`.

8. **Close Resources**:
   - `my_cursor.close()`: Closes the cursor object to free up database resources.
   - `conn.close()`: Closes the connection to the MySQL server.
