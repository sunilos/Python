Here's the code with added comments, followed by a brief explanation:

```python
# Example to Create Table in Database
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Create tables using Python functions and the MySQL connector

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

# Execute an SQL command to create a table named 'student'
cursor.execute("""
CREATE TABLE student (
    sid INT PRIMARY KEY AUTO_INCREMENT,     # 'sid' column: integer, primary key, auto-incremented
    StudentName VARCHAR(255),               # 'StudentName' column: variable character string with max length 255
    RollNo VARCHAR(255)                     # 'RollNo' column: variable character string with max length 255
)
""")

# Execute an SQL command to create a table named 'Registeration'
cursor.execute("""
CREATE TABLE Registeration (
    regid INT PRIMARY KEY AUTO_INCREMENT,   # 'regid' column: integer, primary key, auto-incremented
    Firstname VARCHAR(255),                 # 'Firstname' column: variable character string with max length 255
    LastName VARCHAR(255),                  # 'LastName' column: variable character string with max length 255
    Email VARCHAR(255),                     # 'Email' column: variable character string with max length 255
    Password VARCHAR(255),                  # 'Password' column: variable character string with max length 255
    MobileNumber VARCHAR(255),              # 'MobileNumber' column: variable character string with max length 255
    address VARCHAR(255)                    # 'address' column: variable character string with max length 255
)
""")

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

4. **Create Tables**:
   - `cursor.execute(...)`: Executes SQL commands to create two tables:
     - `student`: Contains columns for student ID (`sid`), name (`StudentName`), and roll number (`RollNo`). The `sid` column is an auto-incrementing primary key.
     - `Registeration`: Contains columns for registration ID (`regid`), first name (`Firstname`), last name (`LastName`), email (`Email`), password (`Password`), mobile number (`MobileNumber`), and address (`address`). The `regid` column is an auto-incrementing primary key.

5. **Close Resources**:
   - `cursor.close()`: Closes the cursor object to free up database resources.
   - `conn.close()`: Closes the connection to the MySQL server.