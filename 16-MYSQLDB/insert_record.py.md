
```python
# Example of Insert Record in Table
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Insert Data into table

from mysql.connector import connection

# Establish a connection to the MySQL server and select the database
conn = connection.MySQLConnection(
    user='root',            # MySQL username
    password='root',        # MySQL password
    host='localhost',       # Database server address (localhost for local server)
    charset='utf8',         # Character set for encoding
    database='testdb'       # Name of the database to connect to
)
    
# SQL query to insert a single record into the 'student' table
# The values for 'Studentname', 'RollNo', and 'StudentEmail' are provided in the query
sql_insert = "Insert into student(Studentname, RollNo, StudentEmail) values ('John', '0206ca121', 'john@gmail.com')"

# Create a cursor object to interact with the database
my_cursor = conn.cursor()

# Execute the SQL query
my_cursor.execute(sql_insert)

# Commit the transaction to make changes persistent in the database
conn.commit()

# Print confirmation message
print("Data Successfully Inserted")

# Close the connection to the MySQL server
conn.close()
```

### Brief Explanation:

1. **Import Module**:
   - `from mysql.connector import connection`: Imports the `connection` object from the `mysql.connector` module to handle MySQL database connections.

2. **Establish Database Connection**:
   - `conn = connection.MySQLConnection(...)`: Creates a connection to the MySQL server with specified parameters:
     - `user='root'`: MySQL username.
     - `password='root'`: MySQL password.
     - `host='localhost'`: Host address of the MySQL server.
     - `charset='utf8'`: Character set for the connection.
     - `database='testdb'`: Database to connect to.

3. **Define SQL Query for Inserting a Single Record**:
   - `sql_insert = "Insert into student(Studentname, RollNo, StudentEmail) values ('John', '0206ca121', 'john@gmail.com')"`: Defines the SQL query for inserting a single record into the `student` table with specified values for `Studentname`, `RollNo`, and `StudentEmail`.

4. **Create Cursor Object**:
   - `my_cursor = conn.cursor()`: Creates a cursor object to interact with the database.

5. **Execute SQL Query**:
   - `my_cursor.execute(sql_insert)`: Executes the SQL query to insert the record into the `student` table.

6. **Commit the Transaction**:
   - `conn.commit()`: Commits the transaction to make the changes permanent in the database.

7. **Print Confirmation**:
   - `print("Data Successfully Inserted")`: Prints a confirmation message indicating that the data has been successfully inserted.

8. **Close Connection**:
   - `conn.close()`: Closes the connection to the MySQL server to free up resources.
