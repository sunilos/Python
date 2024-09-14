Here's the code with added comments, followed by a brief explanation:

```python
# Delete Data From Table By Id
# Example to Delete Record from Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#  

# Import the connection object from the mysql.connector module
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

# Execute an SQL command to delete a record from the 'student' table where 'sid' is 1
cursor.execute("DELETE FROM student WHERE sid = '1'")

# Commit the transaction to make changes persistent in the database
conn.commit()

# Print a confirmation message
print("One record Deleted")

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

4. **Delete Record**:
   - `cursor.execute("DELETE FROM student WHERE sid = '1'")`: Executes an SQL command to delete the record from the `student` table where the `sid` column matches the value `1`.

5. **Commit Transaction**:
   - `conn.commit()`: Commits the transaction, making the deletion permanent in the database.

6. **Print Confirmation**:
   - `print("One record Deleted")`: Prints a confirmation message indicating that one record has been deleted.

7. **Close Resources**:
   - `cursor.close()`: Closes the cursor object to free up database resources.
   - `conn.close()`: Closes the connection to the MySQL server.