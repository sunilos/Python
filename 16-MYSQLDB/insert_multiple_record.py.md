
```python
# Example to Insert multiple records in table 
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

# Insert multiple records into the table

from mysql.connector import connection

# Establish a connection to the MySQL server and select the database
conn = connection.MySQLConnection(
    user='root',            # MySQL username
    password='root',        # MySQL password
    host='localhost',       # Database server address (localhost for local server)
    charset='utf8',         # Character set for encoding
    database='testdb'       # Name of the database to connect to
)

# SQL query to insert multiple records into the 'student' table
# Values for 'Studentname', 'RollNo', and 'StudentEmail' are provided in a list
conn.cursor().executemany(
    "insert into student(Studentname, RollNo, StudentEmail) values (%s, %s, %s)",
    [
        ('Peter', '0206cs122', 'a@gmail.com'),
        ('Amy', '0206cs125', 'b@gmail.com'),
        ('Hannah', '0206cs126', 'c@gmail.com'),
        ('Michael', '0206cs127', 'd@gmail.com'),
        ('Sandy', '0206cs128', 'e@gmail.com'),
        ('Viola', '0206cs129', 'f@gmail.com')
    ]
)

# Commit the transaction to make changes persistent in the database
conn.commit()

# Print confirmation message
print("Multiple Data Successfully Inserted")

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

3. **Define SQL Query for Inserting Multiple Records**:
   - `conn.cursor().executemany(...)`: Uses the `executemany` method to insert multiple records into the `student` table.
     - SQL Query: `"insert into student(Studentname, RollNo, StudentEmail) values (%s, %s, %s)"`: Defines the query for inserting data into `Studentname`, `RollNo`, and `StudentEmail` columns.
     - Data: A list of tuples where each tuple represents a record to be inserted.

4. **Commit the Transaction**:
   - `conn.commit()`: Commits the transaction to make the changes permanent in the database.

5. **Print Confirmation**:
   - `print("Multiple Data Successfully Inserted")`: Prints a confirmation message indicating that the data has been successfully inserted.

6. **Close Connection**:
   - `conn.close()`: Closes the connection to the MySQL server to free up resources.
