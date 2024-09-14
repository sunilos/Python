Here's the code with added comments, followed by a brief explanation:

```python
# Example to show limited records using LIMIT Clause
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Example to show limited records using LIMIT Clause
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
my_cursor = conn.cursor()

# SQL query to fetch the first 4 records from the 'student' table
my_cursor.execute("SELECT * FROM student LIMIT 4")

# Fetch all records from the executed query
my_result = my_cursor.fetchall()

# Iterate through the fetched records and print each record
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

3. **Create Cursor Object**:
   - `my_cursor = conn.cursor()`: Creates a cursor object to execute SQL commands.

4. **Define SQL Query**:
   - `my_cursor.execute("SELECT * FROM student LIMIT 4")`: Executes an SQL query to select the first 4 records from the `student` table. The `LIMIT` clause restricts the number of records returned.

5. **Fetch Results**:
   - `my_result = my_cursor.fetchall()`: Fetches all records returned by the executed query (up to 4 records).

6. **Print Results**:
   - `for x in my_result: print(x)`: Iterates through the fetched records and prints each record.

7. **Close Resources**:
   - `my_cursor.close()`: Closes the cursor object to free up database resources.
   - `conn.close()`: Closes the connection to the MySQL server.